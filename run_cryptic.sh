python -m inference --protein_path cryptic_test/5uoj.pdb \
                    --complex_name "5uoj_octylglucoside" \
                    --ligand cryptic_test/octylglucoside.sdf \
                    --out_dir cryptic_test/ \
                    --inference_steps 20 \
                    --samples_per_complex 40 \
                    --batch_size 10 \
                    --actual_steps 18 \
                    --no_final_step_noise