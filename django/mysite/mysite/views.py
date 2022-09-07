#i have created this file
from  django.http import HttpResponse
from django.shortcuts import render
import subprocess
def index(request):
	
	return render(request,'index.html')
def robots(request):
	return HttpResponse('''
		<p><a href="https://www.w3.org/" target="_blank"><button type="button">W3!</button></a>
		<a href="https://www.w3schools.com/html/default.asp" target="_blank"><button type="button">W3 HTML</button></a>
		<a href="https://www.google.com/" target="_blank"><button type="button">Google!</button></a>

<a href="https://www.hackerrank.com/" target="_blank"><button type="button">Hackerrank!</button></a>

<a href="https://www.codechef.com/"target="_blank"><button type="button">Codechef!</button></a></p>
<a href="/"><button type="button">back</button>''')
	

def about(request):
	return HttpResponse('''this is about of the website
		<a href="/"><button type="button">back</button></a>''')
def analyzer(request):
	djtext=request.POST.get('text','default')
	removepunc=request.POST.get('removepunc','off')
	lowercase=request.POST.get('lowercase','off')
	uppercase=request.POST.get('uppercase','off')
	extra_space=request.POST.get('extra_space','off')
	newline=request.POST.get('newline','off')
	charcount=request.POST.get('charcount','off')
	result1=0


	if removepunc=="on":


		analyzed=djtext
		result=""
		temp = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
		for ele in analyzed:
			if ele not in temp:
				result+=ele
		djtext=result
		

	if uppercase=="on":
		result=""
		
		for ele in djtext:
			result+=ele.upper()
		djtext=result


	if lowercase=="on":
		result=""
		
		for ele in djtext:
			result+=ele.lower()
		djtext=result
	
	if extra_space=="on":
		result=""
		
		for i ,ele in enumerate(djtext):
			try:
				if not (djtext[i]==" " and djtext[i+1]==" "):
					result+=ele
			except:
				pass
		djtext=result
		

	if newline=="on":
		result=""
		
		for ele in djtext:
			if ele!="\n" and ele!="\r":
				result+=ele
		djtext=result
		

	if charcount=="on":
		for ele in djtext:
			if ele!="\n" and ele!=" ":
				result1+=1
		
	params={'analyzed_text':djtext,'count':result1}
	return render(request,'analyze.html',params)


	if (removepunc!='on' and lowercase!="on" and uppercase!="on" and extra_space!="on" and newline!="on"):
		return render(request,'index.html')
def vowel(request):
	v_text=request.POST.get('vowel_input','default')
	vowel_checker=request.POST.get('vowel_checker','off')
	if vowel_checker=="on":
		temp=""
		for ele in v_text:
			if ele in ("aeiouAEIOU"):
				temp+=ele
		t1=len(v_text)
		t2=len(temp)
		t3=t1-t2
		param={'original':v_text,'analyzed_text':temp,'total_text':t1,'total_vowel':t2,'vowel_free_ch':t3}
		print(temp)
		return render(request,'check_vowel.html',param)
	else:
		return render(request,'check_vowel.html')

def syllabus(request):
	linkadd=request.POST.get('linkadd','default')
	addlinkbt=request.POST.get('addlinkbt','off')
	# print(linkadd)
	# print(addlinkbt)
	t=linkadd
	if len(linkadd)!=0 and addlinkbt!='off':
		with open("C:\\Users\\BAD-BOY\\Desktop\\django\\mysite\\templates\\link.txt",'a') as file:
			file.write("\n")
			file.write(t)	
		file.close()
		dict1={'purpose':'add important link for future use','value':linkadd}


		return render(request,'sallyabus.html',dict1)
	else:
		return render(request,'sallyabus.html')



