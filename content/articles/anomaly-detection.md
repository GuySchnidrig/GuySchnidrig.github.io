Title: Anomaly detection
Date: 2025-03-01 
Modified: 2025-03-01
Category: Blog
Tags: machine-learning, surveillance, antibiotic use, veterinary, cattle 
Slug: anomaly-detection
Authors: Guy Schnidrig
Summary: Anomaly detection in IS ABV.

I am delighted to announce the publication of my latest research paper, titled “Anomaly detection in the veterinary antibiotic prescription surveillance system (IS ABV)” in Preventive Veterinary Medicine. In this paper we present a method for the detection of anomalies in the Swiss antibiotic prescription monitoring system.

![anomaly_pic](images/FigureAnomaly.png)

Antibiotic resistance is one of the major concerns in veterinary and human medicine and poses a considerable threat to both human and animal health. It has been shown that over- or misuse of antibiotics is one of the primary drivers of antibiotic resistance. To develop the surveillance of antibiotic use, Switzerland introduced the "Informationssystem Antibiotika in der Veterinärmedizin" (IS ABV) in 2019, mandating electronic registration of antibiotic prescriptions by all veterinarians in Switzerland. However, initial data analysis revealed a considerable amount of implausible data entries, potentially compromising data quality and reliability. These anomalies may be caused by input errors, inaccuracies, incorrect or aberrant master data or data transmission and make analysis impossible. To address this issue efficiently, we propose a two-stage anomaly detection framework utilizing machine learning algorithms. With this methodology, we identified 22,816 anomalies from a total of 1,994,170 prescriptions in cattle (1.1%). Random Forest achieved a ROC-AUC score of 0.994, (95% CI: 0.992, 0.995) and a F1-Score of 0.962 (95% CI: 0.958, 0.966) for single treatments. If applied regularly to uploaded prescriptions, it should reduce input errors over time, improving the validity of the data in the long term. Test

I am grateful for the support and guidance of my mentor and colleagues, and I hope that this research will inspire further exploration and innovation with IS ABV. I am happy to share these findings with anyone who is interested and look forward to engaging discussions and collaborations.

Here you can read the [full paper](https://www.sciencedirect.com/science/article/pii/S0167587724001776).
