from download_gaceta import download_pdf
from gacetachat import embeddings_to_chats
# from twitter import post_tweet 

## download INPUT
download_pdf()


## Create embeddings
## Load embeddings
## prompt to answer


tweet = embeddings_to_chats(f"""
Crea un resumen humorístico de las 3 noticias más importantes de la Gazeta de hoy en un lenguaje sencillo. 
Usa menos de 280 caracteres por noticia. Sé divertido y memorable, informando de forma simple y jocosa. 
Dirígete al público costarricense. 
Usa emojis. No digas cosas redundantes.

Ejemplo:
¡El tren eléctrico vuelve! Ahora sí, después de años, el tren vuelve a rodar por Costa Rica 🚂🎉
Se declara alerta roja por contaminación en el río Virilla. ¡Cuidado al bañarse! 🚫💦
Los chicos del fútbol ganaron el partido de hoy. ¡Qué jugada! ¡Qué partidazo! ⚽🏆

o

1: 🤩 La Municipalidad de Nandayure cede 1515 m2 para usos comunales! 🐠 Incentivando a la comunidad a involucrarse y contribuir al desarrollo y bienestar local. 
2: 🤩 Fabián Dobles Rodríguez recibe el mayor galardón de Benemérito de las Letras Patrias📝 por su aporte a la literatura nacional y la obra de sus predecesores. 
3: 🤬 Costa Rica incluida en el Catálogo de países sin el mejor régimen fiscal. 🤩 Pero hay un proyecto de ley para lograr la exclusión e incluye rentas provenientes del extranjero. 💪 ¡Es nuestro momento de actuar!

o
¡La Municipalidad de Nandayure donará un terreno para salón comunal! 🤩🏡
La Asamblea Legislativa otorga el Benemérito de las Letras Patrias a Fabián Dobles Rodríguez, un escritor de singulares méritos en el campo de la novela y el cuento 🎉📚
La Notaría del Estado confeccionará la escritura de traspaso del bien inmueble, para que su obra literaria siga viva 📝📃
""", "input", debug=True)


## POST TWEET
# post_tweet(tweet)