python -m inference --protein_path cryptic_test/1w50_apo.pdb \
                    --complex_name "1w50_isophthalamide" \
                    --ligand cryptic_test/isophthalamide.sdf \
                    --out_dir cryptic_test/ \
                    --inference_steps 20 \
                    --samples_per_complex 40 \
                    --batch_size 10 \
                    --actual_steps 18 \
                    --no_final_step_noise