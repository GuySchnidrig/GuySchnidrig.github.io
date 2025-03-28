Title: Cattle Classification
Date: 2025-03-01
Category: Blog
Tags: veterinary, cattle, machine-learning, surveillance
Slug: cattle-classification
Summary: Classification of swiss cattle farms

While many countries have registries of livestock farms, obtaining detailed information on their primary production types can still be a challenge. For example, for Swiss farms registered as keeping cattle, a distinction can only be made between milk-producing and non-milk-producing farms. However, a better differentiation of production types would significantly improve the planning and evaluation of cattle disease surveillance.
This study aimed to address this gap by defining five primary cattle production types: calf fattening, dairy cattle, cattle fattening, rearing cattle, and suckler cows. By working with experts and cantonal Veterinary Offices, we collected data from 618 reference farms across 14 cantons and integrated information from three national databases. This allowed us to train machine learning models to classify these production types more accurately.

![anomaly_pic](images/pca_farm_types.png)

The Random Forest model stood out with an 𝐚𝐜𝐜𝐮𝐫𝐚𝐜𝐲 𝐨𝐟 𝟎.𝟗𝟏𝟒 (95% CI: 0.890, 0.938) and an 𝐅𝟏-𝐒𝐜𝐨𝐫𝐞 𝐨𝐟 𝟎.𝟖𝟕𝟗 (95% CI: 0.841, 0.913). Our model enables a reproducible, year-to-year classification of Swiss cattle farms, improving the efficiency of disease surveillance.

![anomaly_pic](images/model_Randomforest_shap_fig.png)

Our methodology is adaptable to other countries and datasets, providing a scalable solution for targeted disease surveillance and perhaps even benchmarking antibiotic use for the benefit of veterinary authorities.

You can read the full paper [here](https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2025.1517173/full).


