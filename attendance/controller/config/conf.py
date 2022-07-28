import sys
import os
sys.path.append('../')

def config(ficha,timing):
    import shutil
    from controller.path import path
    import json
    # Hacemos el proceso de conversion del timing para el .Json
    hour = '0'
    minutes = '0'
    # Ponemos un  0 si es menor a 10 en ambos casos 
    # para que el .Json lea bien el tiempo
    if timing[0] <= 9:
        hour += str(timing[0])
    else:
        hour = timing[0]
        
    if timing[1] <= 9:
        minutes += str(timing[1]) 
    else:
        minutes = timing[1]
    # Juntamos ambos resultados 
    classTime = f'{hour}:{minutes}'
    print(classTime)
    # C:\Users\Proyecto\Desktop\attendance\
    mainPath = path()
    # De donde proviene el archivo
    originalPath = mainPath + 'controller\\config\\config.json'
    # A donde va el archivo
    movePath = mainPath + 'model\\datasets\\attendance_system_dataset\\'+ ficha +'\\config\\config.json'
    # Moviendo el archivo
    shutil.copyfile(originalPath, movePath)
    
    # Cambiando los valores de config
    datasetPath = 'datasets/attendance_system_dataset'
    dbPath = datasetPath + '/' + ficha + '/database/attendance.json'
    encodingsPath = datasetPath + '/' + ficha + '/output/encodings.pickle'
    recognizerPath = datasetPath + '/' + ficha + '/output/recognizer.pickle'
    lePath = datasetPath + '/' + ficha + '/output/le.pickle'
    # que config vamos a abrir y editar
    jsonFile = open(movePath,"r")
    dataJson = json.load(jsonFile)
    jsonFile.close()
    
    jsonFile = open(movePath,"w")
    # Cambiamos los valores del config por los que necesitamos
    dataJson["class"] = ficha
    dataJson["db_path"] = dbPath
    dataJson["encodings_path"] = encodingsPath
    dataJson["recognizer_path"] = recognizerPath
    dataJson["le_path"] = lePath
    dataJson["timing"] = classTime
    
    json.dump(dataJson, jsonFile)
    jsonFile.close()

    

    newPath = mainPath + '\\model'
    # Inicializamos la DB
    os.chdir(newPath)
    os.system('python initialize_database.py --conf datasets/attendance_system_dataset/'+ ficha +'/config/config.json')