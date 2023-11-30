from ultralytics import YOLO

# Carregando o modelo
model = YOLO('best.pt')

# Rodando a inferência
results = model(source="flow.mp4", show=True, conf=0.6, save=True) #Se você quiser testsr com a webcam, troque o "flow.mp4" para 0
