# Cómo hacer peticiones a APIs con Python
# con y sin dependencias

# 1. Sin dependencias (DIFICIL y sin dependencias)
import urllib.request #permite abrir una url
import json #transforma la respuesta a json

DEEPSEEK_API_KEY = "xxx"

api_posts = "https://jsonplaceholder.typicode.com/posts/" #esta es la api

try:
  response = urllib.request.urlopen(api_posts) #abrimos la url
  data = response.read()  #leemos la respuesta
  json_data = json.loads(data.decode('utf-8')) #decodificamos la respuesta a json
  print(json_data)
  response.close() #cerramos la respuesta o la pestaña
except urllib.error.URLError as e:
  print(f"Error en la solicitud: {e}")


# 2. Con dependencia (requests) (FACIL)
import requests

print("\nGET:")
api_posts = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(api_posts)
response_json = response.json()
print(response_json[0]) #imprimimos el primer post

# 3. Un POST
print("\nPOST:")
try:
  response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={
      "title": "foo",
      "body": "bar",
      "userId": 1
    })
  print(response.status_code)
except requests.exceptions.RequestException as e:
  print(f"Error en la solicitud: {e}")

# 4. Un PUT (actualizar) Put-> reemplaza todo el objeto, Patch-> actualiza solo los campos indicados
print("\nPUT:")
try:
  response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={
      "title": "foo",
      "body": "bar",
      "userId": 1,
    })
  print(response.status_code)
except requests.exceptions.RequestException as e:
  print(f"Error en la solicitud: {e}")

# Usar la API de GPT-4o de OpenAI
# Ref: https://platform.openai.com/docs/api-reference/making-requests

OPENAI_KEY = "sk-XXXXXXXX"

import json

def call_openai_gpt(api_key, prompt):
  url = "https://api.openai.com/v1/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": prompt}]
  }

  response = requests.post(url, json=data, headers=headers)
  return response.json()

api_response = call_openai_gpt(OPENAI_KEY, "Escribe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2)) #ve la estructura de la respuesta

print(api_response["choices"][0]["message"]["content"])

# Llamar a la API de DEEPSEEK

import json

def call_deepseek(api_key, prompt):
  url = "https://api.deepseek.com/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": prompt}]
  }

  response = requests.post(url, json=data, headers=headers)
  print(response.json())
  return response.json()

api_response = call_deepseek(DEEPSEEK_API_KEY, "Escribe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])