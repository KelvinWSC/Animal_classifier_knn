# Animal Classifier
a
This is a practice to use k-NN algorithm to classify animals.

The same technique can be used to predict customer behaviour, product preference, voting tendency, possibility of fraud etc.

## **Goal**
To develop a model, using k-NN algorithm and the dataset given by a zoo, to classify animals into correct class type based on the observable traits of the animal.

## **Dataset**
The dataset consists of 101 animals from a zoo. There are 16 variables with various traits to describe the animals.
![image](https://user-images.githubusercontent.com/80243823/122639281-9d6e9100-d12b-11eb-91ba-25b8156122ce.png)

The 7 Class Types are: Mammal, Bird, Reptile, Fish, Amphibian, Bug and Invertebrate
![image](https://user-images.githubusercontent.com/80243823/122639347-ea526780-d12b-11eb-968a-b404ec45fe25.png)

## **k-NN algorithm**
The algorithm can be summarized as follows,

![image](https://user-images.githubusercontent.com/80243823/122639675-bed07c80-d12d-11eb-94e4-efa2135d8826.png)

Say we have 3 categories, yellow, green and orange, and we want to know which category the grey spot belongs to.

![image](https://user-images.githubusercontent.com/80243823/122639716-03f4ae80-d12e-11eb-88f2-76b45ddbe7ae.png)

We then calculate the distances of the grey spot with all other spots

![image](https://user-images.githubusercontent.com/80243823/122639739-2be41200-d12e-11eb-949d-dd2d85f120b6.png)

Take the n nearest neighbours

![image](https://user-images.githubusercontent.com/80243823/122639781-63eb5500-d12e-11eb-9725-267fadb3a93f.png)

Predict the category the grey spot based on the results of the n nearest neighbours

## **Model Construction**

### **Data Cleansing**

First I read the csv file and drop the column 'animal_name', as it is irrelevant for the model. Then I check if there is any missing value in the dataset.

![image](https://user-images.githubusercontent.com/80243823/122639875-01df1f80-d12f-11eb-8024-4d0dabfd4856.png)

![image](https://user-images.githubusercontent.com/80243823/122639958-67cba700-d12f-11eb-99ff-c1487e586ded.png)

As the dataset has been cleansed already, I then specify 'class_type' as the target the model has to predict, and the rest of the dataset as the information for the prediction.
Also, I split the dataset into training and testing set under 80/20 ratio.
![image](https://user-images.githubusercontent.com/80243823/122640117-40290e80-d130-11eb-83f0-1adcaec81112.png)


### **Model Performance**

Instead of training 1 model, I train 30 models (from 1-NN to 30-NN) and compare their performances based on accuracy.

![image](https://user-images.githubusercontent.com/80243823/122640198-b9c0fc80-d130-11eb-9f3b-d129b2cfd24c.png)
![image](https://user-images.githubusercontent.com/80243823/122640208-c80f1880-d130-11eb-8fbc-0f04f020550d.png)

For this dataset, using 1-NN (finding the most similar animal class and predict the animal as that class) yields the highest accuracy.
However, for practice purposes, I employ 5-NN as the final model.

p.s. 1-NN usually is an overfitting model. In order to reduce the model's sensitivity to extreme values, higher NN is applied instead.

### **Testing and Transforming Numeric Results to English**

As the actual animal class names are stored in a separate csv file, 

![image](https://user-images.githubusercontent.com/80243823/122639347-ea526780-d12b-11eb-968a-b404ec45fe25.png)

A dictionary is created to parse the class number into class name,
![image](https://user-images.githubusercontent.com/80243823/122642146-7c15a100-d13b-11eb-8301-f778b6c1b00d.png)

Mock-up data to test the model,
![image](https://user-images.githubusercontent.com/80243823/122642291-4329fc00-d13c-11eb-8818-c2320e1005d7.png)

Results,

![image](https://user-images.githubusercontent.com/80243823/122642339-9734e080-d13c-11eb-8aa5-50a27ee0ba9f.png)

![image](https://user-images.githubusercontent.com/80243823/122642347-a025b200-d13c-11eb-973b-e1b4e5e9cfc2.png)
