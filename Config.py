#Config file
class Config:
    random_state = 42
    cross_val_folds = 10
    presence_threshold = 0.7

    #Training specific parameters
    n_epochs = 80
    batch_size=64
    gaussian_noise_scale = 0.01

    
    #Directory to save models 
    model_save_dir = 'Models_AKI_1_Bootstrapping'


    #Directory to save all metrics
    metrics_save_dir = 'Metrics_AKI_1_Bootstrapping'
    
    #Folder to save all iterations folder
    bootstrap_iter_dir = 'BootstrapIterations_1'