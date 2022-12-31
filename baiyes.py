#Creating Dataframe
weather = ['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy']
temp = ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']
play = ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

df = pd.DataFrame({'weather':weather, 'temp':temp, 'play':play})
print(df)

#Calculating Probabilities
#P(Yes)
prob_yes = (df.play == 'Yes').sum()/len(df.play)

#P(No)
prob_no = (df.play == 'No').sum()/len(df.play)

#P(Overcast | Yes)
prob_overcast_yes = (df[(df.play == 'Yes') & (df.weather == 'Overcast')]).count()/ (df[df.play == 'Yes']).count()

#P(Mild | Yes)
prob_mild_yes = (df[(df.play == 'Yes') & (df.temp == 'Mild')]).count()/ (df[df.play == 'Yes']).count()

#P(Overcast | No)
prob_overcast_no = (df[(df.play == 'No') & (df.weather == 'Overcast')]).count()/ (df[df.play == 'No']).count()

#P(Mild | No)
prob_mild_no = (df[(df.play == 'No') & (df.temp == 'Mild')]).count()/ (df[df.play == 'No']).count()

#Calculating Probability of Input
prob_input_yes = prob_yes * prob_overcast_yes * prob_mild_yes
prob_input_no = prob_no * prob_overcast_no * prob_mild_no

#Making Prediction
if prob_input_yes > prob_input_no:
    print("The given input belongs to the class Yes")
else:
    print("The given input belongs to the class No")

#slip 4
