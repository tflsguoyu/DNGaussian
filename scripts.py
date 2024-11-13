import os

N = 8
objects = ["fish", "eygptian", "flower", "house", "pumpkin", "santa", "squirrel", "strawberry"]

for obj in objects:
    # cmd = f"python dpt/get_depth_map_for_other.py --root_path ../3dgs_scenes/{N}/{obj}"
    # print(cmd)
    # os.system(cmd)

    cmd = f"python train_other.py --dataset DTU -s ../3dgs_scenes/{N}/{obj} --model_path ../3dgs_scenes/{N}/{obj} --n_sparse 8 --iterations 15000 --lambda_dssim 0.6 --densify_grad_threshold 0.001 --prune_threshold 0.01 --densify_until_iter 6000 --percent_dense 0.1 --position_lr_init 0.0016 --position_lr_final 0.000016 --position_lr_max_steps 5500 --position_lr_start 500 --error_tolerance 0.01 --opacity_lr 0.05 --scaling_lr 0.003 --shape_pena 0.005 --opa_pena 0.001 --scale_pena 0.005"
    print(cmd)
    os.system(cmd)

    cmd = f"python render_json.py -m ../3dgs_scenes/{N}/{obj} -s ../3dgs_scenes/{N}/{obj} --out ../3dgs_scenes/{N}/{obj}/output --white_background"
    print(cmd)
    os.system(cmd)
    exit()
