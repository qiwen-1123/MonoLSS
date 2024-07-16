def wandb_dict_converter(Car_res: dict):
    'convert Car_res to a wandb dict'
    wandb_dict = {}
    keys = ['easy', 'moderate', 'hard']
    
    for key, values in Car_res.items():
        if '@' in key:
            base_key, threshold = key.split('@')
            for i, value in enumerate(values):
                new_key = f"{base_key}_{threshold}_{keys[i]}"
                wandb_dict[new_key] = value
        else:
            for i, value in enumerate(values):
                new_key = f"{key}_{keys[i]}"
                wandb_dict[new_key] = value
    
    return wandb_dict