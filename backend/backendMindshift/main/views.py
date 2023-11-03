from django.shortcuts import render
from django.http import HttpResponse
from mlModel import word_recog
from mlModel import bipolar_model
# Create your views here.
def index(request):
    return render(request,'index.html')
def userBipolar(request):
    if request.method=='POST':
        file=request.FILES.get('file')       
        
    dataFile=["i am happy","Juuuuuuuuuuuuuuuuussssst Chillin!!","thanks to all the haters up in my face all day! ","life is wonderfull","be cheerfull","i am miserable","just laughing","kicking"]
    happyNum=0
    sadNum=0
    for d in dataFile: 
       if word_recog.analyze_sentiment(d)==True:
           print("this was views",d)
           happyNum+=1
       else:
           sadNum+=1;    
    if bipolar_model.isBipolar(happyNum,sadNum):
        print("the person is suffering from bipolar")
    else:
        print("the person is ok")    
    return render(request,'userBipolar.html')