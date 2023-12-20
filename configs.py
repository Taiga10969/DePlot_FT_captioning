
class DePlot_FT_Config():
    def __init__(self):
        
        self.wandb = False
        self.project_name = f"DePlot_FT_training_001"
        self.is_DataParallel = True
        self.save_param_time = 1

        self.batch_size = 2
        self.num_eposh = 20

        self.clip_value = 0.5

        self.max_length = 128

        self.lr = 5e-4  #学習率
        self.weight_decay = 0.1
        self.t0 = 20
