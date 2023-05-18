
# coding: utf-8

# In[1]:


import pandas as pd
from test_code.extractor1 import extract_text_from_doc,extract_text
import joblib


# In[2]:


def predict(doc):
	#doc="input\\input.docx"

	#text_data=extract_text_from_doc(doc)
	text_data=extract_text(doc)
	text_data=text_data.replace(',',"")
	text_data=text_data.lower()
	text_data=text_data.split(" ")


	# In[3]:      


	print(text_data)
	print("\nText length:\n",len(text_data))


	# In[4]:


	opnss=['imaginative','insightful','curious','creative','outspoken','straightforward','direct','receptive','open-minded','adventurous']
	cons=['thoughtful','goal-oriented','ambitious','organised','mindful','vigilant','control','disciplined','reliable','responsible']
	extr=['cheerful','sociable','talkative','assertive','outgoing','energetic','extroverted','friendly','enthusiastic','outspoken']
	agree=['trustworthy','altruism','kind','affectionate','cooperative','empathetic','modest','sympathetic','compliant','tender-minded']
	neuro=['calm','strong hearted','collected','balanced','peaceful','tranquil','strong-willed','stable']


	# In[5]:

                                                                                                                                                               
																																							   
	opnss_val=0
	cons_val=0
	extr_val=0
	agree_val=0
	neuro_val=0
	temp=0
	age=0


	# In[6]:


	for i in text_data:
		temp=temp+1
		if i in opnss:
			if opnss_val<10:
				opnss_val=opnss_val+1
		if i in cons:
			if cons_val<10:
				cons_val=cons_val+1
		if i in extr:
			if extr_val<10:
				extr_val=extr_val+1
		if i in agree:
			if agree_val<10:
				agree_val=agree_val+1
		if i in neuro:
			if neuro_val<10:
				neuro_val=neuro_val+1


	# In[7]:


	print("\nValues generated from resume:\n")
	#print(opnss_val,cons_val,extr_val,agree_val,neuro_val)
	print("openness:",opnss_val)
	print("conscientiousness:",cons_val)
	print("extraversion:",extr_val)
	print("agreeableness:",agree_val)
	print("neuroticism:",neuro_val)


	# In[8]:


	test=pd.DataFrame({'openness':[opnss_val],'neuroticism':[neuro_val],'conscientiousness':[cons_val],
				  'agreeableness':[agree_val],'extraversion':[extr_val],})
	test


	# In[9]:


	file=open("test_code/label.pkl","rb")
	le=joblib.load(file)
	file.close()


	# In[10]:


	file=open("test_code/model_rf.pkl","rb")
	clf_rf=joblib.load(file)
	file.close()


	# In[11]:


	y_pred_rf= clf_rf.predict(test)


	# In[12]:


	out=le.inverse_transform(y_pred_rf)
	#print(y_pred_rf)


	# In[13]:


	"""print("\nOutput:\n",out[0])


	# In[14]:


	file=open("out.txt",'w')
	file.write(out[0])
	file.close()"""
	
	return out[0]
	
#result=predict()
#print(result)

