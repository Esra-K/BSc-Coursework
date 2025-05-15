import json
import codecs
import model

training_data_path = 'train.txt'
test_data_path = 'test.txt'

with open(training_data_path) as training_data_file:
    training_data = json.load(codecs.open('train.txt', 'r', 'utf-8-sig'))

with open(test_data_path) as test_data_file:
    test_data = json.load(codecs.open('test.txt', 'r', 'utf-8-sig'))

model.train(training_data)

corrects = 0
total = len(test_data)

for doc in test_data:
    category = doc.pop('category')
    predicted_category = model.classify(doc)
    if category == predicted_category:
        corrects += 1

accuracy = corrects / total

print('Accuracy: {:.3f}'.format(accuracy))
