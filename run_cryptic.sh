python -m inference --protein_path cryptic_tests/5uoj.pdb \
                    --ligand cryptic_tests/octylglucoside.sdf \
                    --out_dir cryptic_tests/ \
                    --inference_steps 20 \
                    --samples_per_complex 40 \
                    --batch_size 10 \
                    --actual_steps 18 \
                    --no_final_step_noise