
class DePlot_FT_Config():
    def __init__(self):
        
        self.wandb = True     # True or False
        self.project_name = f"FT_test_001"
        self.is_DataParallel = True # True or False
        self.save_param_time = 1

        self.batch_size = 64
        self.num_eposh = 40

        self.clip_value = 0.5

        self.max_length = 128

        self.lr = 1e-4  #学習率
        self.weight_decay = 0.1
        self.t0 = 20
