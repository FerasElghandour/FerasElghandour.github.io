# Figure sources

The portfolio uses existing project artifacts and figures replotted from recorded results. No models were retrained for this presentation update.

- **capacity-results.png:** [recursive-network-capacity-study/results/accuracy_by_size.png](https://github.com/FerasElghandour/recursive-network-capacity-study/blob/main/results/accuracy_by_size.png). Original image, unmodified.
- **tennis-report.png:** [tennis-reinforcement-learning/assets/report-preview.png](https://github.com/FerasElghandour/tennis-reinforcement-learning/blob/main/assets/report-preview.png). Original image, unmodified.
- **vae-comparison.png:** [tabular-vae-comparison/results/reproduction.json](https://github.com/FerasElghandour/tabular-vae-comparison/blob/main/results/reproduction.json). Replotted from the recorded numerical artifact.
- **braking-telemetry.png:** [autonomous-braking-simulation/results/run.csv](https://github.com/FerasElghandour/autonomous-braking-simulation/blob/main/results/run.csv). Replotted from the recorded numerical artifact.
- **fusion-comparison.png:** [sensor-fusion-policy-engine/validation/release-20261017/results.json](https://github.com/FerasElghandour/sensor-fusion-policy-engine/blob/main/validation/release-20261017/results.json). Replotted from the recorded numerical artifact.
- **maintenance-outcomes.png:** [predictive-maintenance/docs/data.json](https://github.com/FerasElghandour/predictive-maintenance/blob/main/docs/data.json). Replotted from the recorded numerical artifact.

The Webots scene is the original results/final_screenshot.png from autonomous-braking-simulation, displayed without alteration. Its Git blob SHA is 2c571342a76ed5500b715100b93a30b48af79706.

vae-training.svg is a new architecture schematic of the documented 30-feature, 2D-latent VAE. It illustrates the model path, rather than an experimental result. Test reconstruction uses the latent mean.

Figure context:

- Capacity: four datasets, ten recorded seeds per cell, native feature order. Shading is one seed standard deviation, not a confidence interval.
- Tennis: the plot is the rolling training score; the 2.067 saved-policy evaluation is a separate historical sequence. One training seed.
- VAE: deterministic mean-latent reconstruction with train-only scaling. MSE values 0.2830780386227613 and 0.3231309277272364.
- Braking: one saved straight-road, static-obstacle simulation. Lines use true_speed_mps and true_distance_m; the marker is the first BRAKING controller state.
- Fusion: mean F1 over three recorded seeds, 1,000 synthetic missions per seed. Dots are individual seed values.
- Maintenance: 29 timely warnings, one early intervention, five missed observed windows, 65 histories censored before the danger window. The 45% threshold was selected on validation. These are observed-window outcomes, not eventual failure coverage.


## Mobile layouts and Tennis clarification

The mobile SVGs replot the same recorded VAE, fusion, maintenance and braking values with larger labels. capacity-overview-mobile.svg summarizes the documented 14/16 balanced-over-random and 5/16 balanced-over-corrected-compute-dense comparison counts; the original four-panel accuracy figure remains linked.

tennis-results.svg and tennis-results-mobile.svg replace the overview preview with separate training and saved-policy evaluation panels. Sources: [training_scores.csv](https://github.com/FerasElghandour/tennis-reinforcement-learning/blob/main/run-seed-0/training_scores.csv), [evaluation_scores.csv](https://github.com/FerasElghandour/tennis-reinforcement-learning/blob/main/run-seed-0/evaluation_scores.csv) and [training_result.json](https://github.com/FerasElghandour/tennis-reinforcement-learning/blob/main/run-seed-0/training_result.json). Training: full-window rolling mean for 875 episodes. Saved checkpoint: episode 634, rolling mean 0.5338000080175698. Evaluation: 100 episodes, mean 2.0670000308007004, learning and exploration off. The panels deliberately use separately labeled y-axis scales. No retraining was performed.

## Mechanism schematics

topology-comparison.svg and its mobile variant are generated from run_grid.topology(8, kind, 0): balanced depth 3, random depth 4, skewed depth 7. They depict feature-group encoders, concatenating merge blocks and the classifier, not experimental outcomes. Feature dimensions vary; Satimage uses nine groups.

shared-policy-mechanism.svg and its mobile variant describe the implemented Actor, Critic and MADDPGAgent classes: shared local actor/critic/replay, 128-transition minibatches and soft target updates with tau 0.01. They do not depict a centralized critic or claim an environment rollout. The runnable examples use explicitly generated inputs.
