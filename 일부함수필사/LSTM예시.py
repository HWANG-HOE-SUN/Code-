from core.Data_processor import DataLoader
from core.train_model import Model

configs = {
    "training": {
        "epochs": 1000,
        "batch_size": 1440
    },
    "model": {
        "loss": "mae",
        "optimizer": "adam",
        "save_dir": "saved_models",
        "layers": [
            {
                "type": "lstm",
                "neurons": 50,
                "input_timesteps": 1,
                "input_dim": 10
            },
            {
                "type": "dense",
                "neurons": 1
            }
        ]
    }
}

# 파일 경로
filename = r'C:\Users\ekdnj\PycharmProjects\PPPLANT\input\Generate_Data.csv'
# 예측할 고장
target_breakdown = "Pump_Breakdown"
# 예측하지 않는 고장
N_target_breakdown = "Valve_Breakdown"
# (하루 = 1440, 이틀 = 2880)
timestep = 1440


def main():
    # 데이터 불러오기
    data = DataLoader(
        filename,
        target_breakdown,
        timestep)
    df = data.mode_split()
    data.fitDataOut(df, target_breakdown)
    print("Data load")

    # 데이터 전처리 및 입출력 분할
    reframed = data.preProcessing(df, target_breakdown, N_target_breakdown)
    train_X, train_y = data.splitData(reframed)
    print("Data preprocessing and split")

    # 모형 생성
    input_dim = train_X.shape[2]
    input_timesteps = train_X.shape[1]
    model = Model()

    # 모델 학습
    model.bulid_model(configs, input_timesteps, input_dim)
    model.train(train_X,
                train_y,
                epochs=configs['training']['epochs'],
                batch_size=configs['training']['batch_size'],
                save_dir=configs['model']['save_dir'])


if __name__ == "__main__":
    main()
