python -m inference --protein_ligand_csv gpcr_eval_experiment.csv \
                    --out_dir gpcr_eval/ \
                    --inference_steps 20 \
                    --samples_per_complex 40 \
                    --batch_size 10 \
                    --actual_steps 18 \
                    --no_final_step_noise