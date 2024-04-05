from googletrans import Translator

# Crear una instancia de la clase Translator
traductor = Translator()


def translateText(text, leng='en'):
  try:
    return traductor.translate(text, dest=leng).text
  except Exception as e:
    return f'Error {e}'


keepAnswering = True

while keepAnswering:
  textToTranslate = input('Introduce el texto a traducir: ')
  outputLanguage = input(
      'Introduce el idima que desea para la traduccion (codigo): ')

  if (textToTranslate):
    print(f'La traduccion de "{textToTranslate}" es:')
    print(f'== {translateText(textToTranslate, outputLanguage)} ==')
  else:
    'Error al traducir :('
  userRes = input('¿Quieres traducir otro texto? (s/n)')
  if (userRes.lower() == 'n'):
    print('Saliendo...')
    break
