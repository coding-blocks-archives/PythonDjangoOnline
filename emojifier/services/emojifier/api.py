from keras.models import model_from_json
import emoji
import pandas as pd
import numpy as np

emoji_dictionary = {
  "0": "\u2764\uFE0F",    # :heart: prints a black instead of red heart depending on the font
  "1": ":baseball:",
  "2": ":beaming_face_with_smiling_eyes:",
  "3": ":downcast_face_with_sweat:",
  "4": ":fork_and_knife:",
}
with open("services/emojifier/model.json", "r") as file:
  model = model_from_json(file.read())
model.load_weights("services/emojifier/model.h5")
model._make_predict_function()
embeddings = {}
with open('services/emojifier/glove.6B.50d.txt', encoding='utf-8') as f:
  for line in f:
    values = line.split()
    word = values[0]
    coeffs = np.asarray(values[1:], dtype='float32')
    embeddings[word] = coeffs

print(model)

def getOutputEmbeddings(X):
  embedding_matrix_output = np.zeros((X.shape[0],10,50))
  for ix in range(X.shape[0]):
    X[ix] = X[ix].split()
    for jx in range(len(X[ix])):
      embedding_matrix_output[ix][jx] = embeddings[X[ix][jx].lower()]
  return embedding_matrix_output

def predict(x):
  X = pd.Series([x])
  emb_X = getOutputEmbeddings(X)
  p = model.predict_classes(emb_X)
  return emoji.emojize(emoji_dictionary[str(p[0])])

if __name__ == "__main__":
  print(predict('hello how are you'))
