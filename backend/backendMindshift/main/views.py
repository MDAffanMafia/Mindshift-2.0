from django.shortcuts import render
from django.http import HttpResponse
from mlModel import word_recog
from mlModel import bipolar_model
from main.models import Post
# Create your views here.
def index(request):
    return render(request,'index.html')
def userBipolar(request):
    if request.method=='POST':
        file=request.FILES.get('file')  
        newFile=Post(content=file)
        newFile.save()     
        print("this")
        f = open("D:\\mindshift\\backend\\backendMindshift\\media\\prodImages\\userData.txt", "r")
        print(f.read())
        wordData=[]
        datafile=f.readlines()
        happyNum=0
        sadNum=0
        status=""
        for line in datafile:
            for word in line.split():
                wordData.insert(word)
        for d in wordData: 
           if word_recog.analyze_sentiment(d)==True:
               print("this was views",d)
               happyNum+=1
           else:
               sadNum+=1;    
        if bipolar_model.isBipolar(happyNum,sadNum):
           status="the person is suffering from bipolar"
           print("the person is suffering from bipolar")
        else:
           status="you are ok"
           print("the person is ok")    
        return render(request,'userBipolar.html',{'curStatus':status}) 
    nostate=""  
    return render(request,'userBipolar.html',{'curStatus':nostate})