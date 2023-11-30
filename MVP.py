from ultralytics import YOLO

# Carregando o modelo
model = YOLO('best.pt')

# Rodando a inferência
results = model(source="flow.mp4", show=True, conf=0.6, save=True)
