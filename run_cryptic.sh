python -m inference --protein_path cryptic_test/3cj0_POO/3cj0_apo.pdb \
                    --complex_name "3cjo_POO" \
                    --ligand_ "CN1CCC[CH](C1)CN(C)C(=O)Cn2c3cc(ccc3c(C4CCCCC4)c2c5ccccc5)C(O)=O" \
                    --out_dir cryptic_test/3cjo_POO/ \
                    --inference_steps 20 \
                    --samples_per_complex 40 \
                    --batch_size 10 \
                    --actual_steps 18 \
                    --no_final_step_noise

