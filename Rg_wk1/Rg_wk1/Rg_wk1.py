
import graphlab

sales = graphlab.SFrame('D:\\ML_Learning\\UW_Regression\\Week1\\kc_house_data.gl\\')
train_data,test_data = sales.random_split(.8,seed=0)

#ft is our X and target is y
#w0 = sum(y)/N - w1*sum(x)/N
#w1 = (sum(yx)-sum(y)sum(x)/N)/(sum(x2)-sum(x)sum(x)/N))
# return intercept and slope
def simple_reg(ft,target):
    #print ft
    #print target
    mx = ft.mean()
    print "mx= ",mx
    my = target.mean()
    print "my = ",my
    ntot = ft.size()
    xy = ft*target
    mxy = xy.mean()
    print "mxy = ",mxy
    x2 = ft*ft
    mx2 = x2.mean()
    print "mx2 = ",mx2
    w1 = ( mxy - mx*my )/(mx2-mx*mx)
    print "slope = ", w1    
    w0 = my - w1 * mx
    print "intecept = ", w0
    return (w0,w1)
test_feature = graphlab.SArray(range(5))
test_output = graphlab.SArray(1 + 1*test_feature)
(intecept,slope) =  simple_reg(train_data['sqft_living'], train_data['price'])
#(intecept,slope) =  simple_reg(test_feature, test_output)
#based on the intecept and slope to predict
def predict(ft,intecept,slope):
    target = slope*ft + intecept
    #print predict
    return target
#calculate rss (residue sum of square)
def get_rss(ft,target,intecept,slope):
    pred = intecept + slope*ft
    residue = target - pred
    rsstmp = residue * residue
    rss = rsstmp.sum()
    print "residue sum of squre = ", rss
    return rss
#rss_price = get_rss(test_feature,test_output,intecept,slope)
my_house_sqrt = 2650
estimate_price = predict(2650,intecept,slope)
print "The estimated price for a house with %d squarefeet is $%.2f" % (my_house_sqrt, estimate_price)
rss_price = get_rss(train_data['sqft_living'],train_data['price'],intecept,slope)
print 'The RSS of predicting Prices based on Square Feet is : ' + str(rss_price)
#predict feature based on target
def inverse_pred(target,intecept,slope):
    ft = (target - intecept)/slope
    return ft
my_house_price = 800000
estimate_sqft = inverse_pred(800000,intecept,slope)
print "The estimated square feet for a house with %d price is %.2f" % (my_house_price, estimate_sqft)
(intecept_bed,slope_bed) =  simple_reg(train_data['bedrooms'], train_data['price'])
rss_bed = get_rss(train_data['bedrooms'],train_data['price'],intecept_bed,slope_bed)
print 'The RSS of predicting Prices based on Bed room is : ' + str(rss_bed)

rss_price = get_rss(test_data['sqft_living'],test_data['price'],intecept,slope)
print 'The RSS of predicting Prices based on Square Feet on test data is : ' + str(rss_price)
rss_bed = get_rss(test_data['bedrooms'],test_data['price'],intecept_bed,slope_bed)
print 'The RSS of predicting Prices based on Bed room on test data is : ' + str(rss_bed)
