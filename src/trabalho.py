import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

st.header("4. Tons de cinza")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
pr = st.slider("Peso do R", 0.01, 1.0, 0.299)
pg = st.slider("Peso do G", 0.01, 1.0, 0.587)
pb = st.slider("Peso do B", 0.01, 1.0, 0.114)
r = img[:, :, 0].astype(float)
g = img[:, :, 1].astype(float)
b = img[:, :, 2].astype(float)
media = ((r + g + b) / 3).astype(np.uint8)
ponderada = ((pr * r + pg * g + pb * b) / (pr + pg + pb)).astype(np.uint8)
col1, col2 = st.columns(2)
col1.image(media)
col2.image(ponderada)

st.header("5. Canais")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
col1, col2 = st.columns(2)
col1.image(img[:, :, 0])
col1.image(img[:, :, 1])
col1.image(img[:, :, 2])
escolhido = st.slider("Canal (0 = R, 1 = G, 2 = B)", 0, 2, 0)
colorido = np.zeros(img.shape, dtype=np.uint8)
colorido[:, :, escolhido] = img[:, :, escolhido]
col2.image(colorido)

st.header("6. Troca de canais")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
para_r = st.slider("Canal que vai para o R (0 = R, 1 = G, 2 = B)", 0, 2, 0)
para_g = st.slider("Canal que vai para o G (0 = R, 1 = G, 2 = B)", 0, 2, 1)
para_b = st.slider("Canal que vai para o B (0 = R, 1 = G, 2 = B)", 0, 2, 2)
troca = img.copy()
troca[:, :, 0] = img[:, :, para_r]
troca[:, :, 1] = img[:, :, para_g]
troca[:, :, 2] = img[:, :, para_b]
st.image(troca)

st.header("16. Granulado")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
intensidade = st.slider("Intensidade do granulado", 0.0, 1.0, 0.3)
ruido = np.random.randint(0, 256, img.shape)
granulado = ((1 - intensidade) * img + intensidade * ruido).astype(np.uint8)
st.image(granulado)

st.header("18. Padrão colorido")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
k = st.slider("k", 1, 20, 4)
peso = st.slider("Peso do padrão", 0.0, 1.0, 0.5)
y, x = np.indices((img.shape[0], img.shape[1]))
padrao = np.zeros(img.shape, dtype=np.uint8)
padrao[:, :, 0] = (x * k) % 256
padrao[:, :, 1] = (y * k) % 256
padrao[:, :, 2] = ((x + y) * k) % 256
mistura = ((1 - peso) * img + peso * padrao).astype(np.uint8)
st.image(mistura)