---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Passionate about improving lives through biomedical engineering, I chose this field to fulfill my lifelong desire to help others. As a Senior Biomedical Engineer focusing on programming, I have successfully completed numerous freelance projects over the past three years. My expertise lies in data analysis, image processing, and signal processing, complemented by a deep understanding of programming languages such as Python and MATLAB.
One of my fundamental interests is leveraging programming to develop advanced diagnosis and prediction systems for various diseases. I aim to create innovative solutions to enhance patient care and outcomes by harnessing my data analysis and signal processing skills.
In addition to my technical capabilities, I have a solid technological background and excel in developing computer-aided design systems for biomedical engineering applications. By combining signal processing techniques with machine learning algorithms, I have successfully contributed to advancing this field.
What truly excites me is the realm of Deep Learning. Its potential to revolutionize healthcare and improve patient outcomes is immense. I am constantly driven to expand my knowledge and expertise in this domain, actively seeking further opportunities to develop my skills.
I firmly believe consistency is the key to success throughout my journey. I have achieved significant milestones in my career by maintaining a steadfast approach and consistently delivering high-quality results.
To further enrich my knowledge and acquire new experiences, I am now preparing to embark on a challenging and rewarding endeavor by pursuing a Ph.D. in Biomedical Engineering. This will enable me to delve deeper into research, contribute to cutting-edge advancements, and make a lasting impact.


# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Physical and Engineering Sciences in Medicine, 2023</div><img src='images/Publications/ADHD.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Potential Biomarker for Early Detection of ADHD Using Phase-Based Brain Connectivity and Graph Theory](https://doi.org/10.1007/s13246-023-01310-y)

**Farhad Abedinzadeh Torghabeh**, Seyyed Abed Hosseini*, Yeganeh Modaresnia.

- This research investigates an efficient strategy for early detection and intervention of attention-deficit hyperactivity disorder (ADHD) in children. ADHD is a neurodevelopmental condition characterized by inattention and hyperactivity/impulsivity symptoms, which can significantly impact a child’s daily life. This study employed two distinct brain functional connectivity measurements to assess our approach across various local graph features. Six common classifiers are employed to distinguish between children with ADHD and healthy control. Based on the phase-based analysis, the study proposes two biomarkers that differentiate children with ADHD from healthy control, with a remarkable accuracy of 99.174%. Our findings suggest that subgraph centrality of phase-lag index brain connectivity within the beta and delta frequency bands could be a promising biomarker for ADHD diagnosis. Additionally, we identify node betweenness centrality of inter-site phase clustering connectivity within the delta and theta bands as another potential biomarker that warrants further exploration. These biomarkers were validated using a t-statistical test and yielded a p-value of under 0.05, which approved their significant difference in these two groups. Suggested biomarkers have the potential to improve the accuracy of ADHD diagnosis and could help identify effective intervention strategies for children with the condition.

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Medical & Biological Engineering & Computing, 2023</div><img src='images/Publications/NewASD.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Hybrid Deep Transfer Learning Based Early Diagnosis of Autism Spectrum Disorder Using Scalogram Representation of Electroencephalography Signals](https://doi.org/10.1007/s11517-023-02959-z)

**Farhad Abedinzadeh Torghabeh**, Yeganeh Modaresnia, Mohammad Hossein Moattar*.

- Early diagnosis of autism spectrum disorder (ASD) plays an important role in the rehabilitation of the patient. This goal necessitates higher-level pattern representation and a strong modeling approach. The proposed approach applies scalogram images of electroencephalography signals for the first purpose and a two-level deep learning architecture for better classification. Scalogram images embed both the temporal and spectral information of the signal. On the other hand, the hybrid deep learning hierarchy of convolutional neural network followed by long short-term memory models both spatial and temporal information of the scalogram image. The approach is evaluated on a dataset of 34 ASD samples and 11 normal cases in without-voice and with-voice conditions. To validate the early diagnosis hypothesis, signals from children older than 5 years are used as the training set, and signals from younger subjects are used as the validation set. The proposed method achieves excellent performance of 99.50% and 98.43% for automatically detecting ASD with and without voice, respectively. This classification performance is higher than most recent reported approaches, and the results show the effectiveness of the approach in early diagnosis of ASD and demonstrate the auditory impact on the diagnosis of autism.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Medicine in Novel Technology and Devices, 2023</div><img src='images/Publications/VoicePD.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Enhancing Parkinson’s Disease Severity Assessment through Voice-Based Wavelet Scattering, Optimized Model Selection, and Weighted Majority Voting](https://doi.org/10.1016/j.medntd.2023.100266)

**Farhad Abedinzadeh Torghabeh**, Seyyed Abed Hosseini*, Elham Ahmadi Moghadam.

- Parkinson's disease (PD) is a neurodegenerative disorder characterized by motor and non-motor symptoms that significantly impact an individual's quality of life. Voice changes have shown promise as early indicators of PD, making voice analysis a valuable tool for early detection and intervention. This study aims to assess and detect the severity of PD through voice analysis using the mobile device voice recordings dataset. The dataset consisted of recordings from PD patients at different stages of the disease and healthy control subjects. A novel approach was employed, incorporating a voice activity detection algorithm for speech segmentation and the wavelet scattering transform for feature extraction. A Bayesian optimization technique is used to fine-tune the hyperparameters of seven commonly used classifiers and optimize the performance of machine learning classifiers for PD severity detection. AdaBoost and K-nearest neighbor consistently demonstrated superior performance across various evaluation metrics among the classifiers. Furthermore, a weighted majority voting (WMV) technique is implemented, leveraging the predictions of multiple models to achieve a near-perfect accuracy of 98.62%, improving classification accuracy. The results highlight the promising potential of voice analysis in PD diagnosis and monitoring. Integrating advanced signal processing techniques and machine learning models provides reliable and accessible tools for PD assessment, facilitating early intervention and improving patient outcomes. This study contributes to the field by demonstrating the effectiveness of the proposed methodology and the significant role of WMV in enhancing classification accuracy for PD severity detection.

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">International Clinical Neuroscience, 2023</div><img src='images/Publications/CNN-ADHD.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[EEG-Based Effective Connectivity Analysis for ADHD Detection Using Color-Coded Granger-Causality Images and Custom Convolutional Neural Network](https://doi.org/10.34172/icnj.2023.12)

**Farhad Abedinzadeh Torghabeh**, Yeganeh Modaresnia, Seyyed Abed Hosseini*.

- Attention deficit hyperactivity disorder (ADHD) is prevalent worldwide, affecting approximately 8-12% of children. Early detection and effective treatment of ADHD are crucial for improving academic, social, and emotional outcomes. Despite numerous studies on ADHD detection, existing models still lack accuracy distinguishing between ADHD and healthy control (HC) children. This study introduces an innovative methodology that utilizes granger causality (GC), a well-established brain connectivity analysis technique, to reduce the required EEG electrodes. We computed GC indexes (GCI) for the entire brain and specific brain regions, known as regional GCI, across different frequency bands. Subsequently, these GCIs were transformed into color-coded images and fed into a custom-developed 11-layer convolutional neural network. The proposed model is evaluated through a five-fold cross-validation, achieving the highest accuracy of 99.80% in the gamma frequency band for the entire brain and an accuracy of 98.50% in distinguishing the theta frequency band of the right hemisphere of ADHD and HC children by only using eight electrodes. The proposed framework provides a powerful automated tool for accurately classifying ADHD and HC children. The study’s outcome demonstrates that the innovative proposed methodology utilizing GCI and a custom-developed convolutional neural network can significantly improve ADHD detection accuracy, improving affected children’s overall quality of life.

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Multimedia Tools and Applications, 2024</div><img src='images/Publications/Diabetes.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Enhancing Multi-class Diabetic Retinopathy Detection Using Tuned Hyper-parameters and Modified Deep Transfer Learning](https://doi.org/10.1007/s11042-024-18506-3)

Yeganeh Modaresnia, **Farhad Abedinzadeh Torghabeh**, Seyyed Abed Hosseini*.

- Diabetes retinopathy (DR) is the primary cause of blindness worldwide. Computer-aided diagnosis methods for early detection of DR fundus images are time and effort-saving and have a low risk of a misdiagnosis compared with a manual diagnosis of DR by clinical experts and ophthalmologists. Recently, transfer learning strategies of pre-trained models have been increasingly employed in medical image detection as a deep learning technique, and they effectively speed up the training phase. However, the effect of image enhancement and hyper-parameter tuning in DR detection was not reported in the literature. Furthermore, conventional transfer learning strategies, while widely employed, have exhibited limitations in achieving high accuracies in this context. Here, we employed the publicly available APTOS dataset for training models. Three different image enhancement techniques, including contrast enhancement, color constancy, and contrast-limited adaptive histogram equalization (CLAHE), are used on DR and its severity detection. Bayesian optimization method was employed for hyper-parameter tuning. Three different pre-trained convolutional neural networks, namely AlexNet, GoogLeNet, and SqueezeNet, are investigated on the binary and multi-classification of DR fundus images. The AlexNet model with tuned training hyper-parameters showed an accuracy of 99.10% for multi-classification of DR. The modified AlexNet + genetic algorithm and tuned hyper-parameters model achieved an impressive accuracy of 99.81% in the same multi-level classification of DR severity. The CLAHE enhancement technique outperforms other techniques in these approaches. The reliable performance of the proposed method would enhance the rapid and robust detection of DR utilizing fundus images to intervene effectively before vision loss occurs.

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Medicine in Novel Technology and Devices, 2024</div><img src='images/Publications/PD_Severity.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[An Efficient Tool for Parkinson’s Disease Detection and Severity Grading Based on Time-Frequency and Fuzzy Features of Cumulative Gait Signals through Improved LSTM Networks](https://www.sciencedirect.com/science/article/pii/S2590093524000134)

**Farhad Abedinzadeh Torghabeh**, Yeganeh Modaresnia, Seyyed Abed Hosseini*.

- Parkinson's disease (PD) is a widespread neurodegenerative condition that affects many individuals annually. Early identification and monitoring of disease progression are crucial to effectively managing symptoms and preventing motor complications. This research proposes an automated PD diagnosis and severity-grading model based on time-frequency and fuzzy features using improved uni-directional and bi-directional long short-term memory networks with sensitive hyperparameters optimization. We utilize vertical ground reaction force signals collected from Physionet's publicly available dataset recorded during regular and dual-task clinical trials of walking measurements. Only the cumulative signal of both feet was then utilized and segmented into 30-s windows without further pre-processing. Subsequently, we extracted only four key time-frequency and fuzzy features from each segment, effectively capturing the signal's inherent uncertainty. Bayesian optimization is employed in both detection and grading approaches to fine-tune the two critical hyperparameters: the initial learning rate and the number of hidden units in the network. The detection phase yields an exceptional accuracy of 99.19%, surpassing state-of-the-art studies with the same dataset. In the grading phase, classification based on the unified PD rating scale values achieves an accuracy of 92.28%. The proposed study delves into the potential of cumulative gait signals as a powerful diagnostic tool for PD, aiming to extract precise and intricate information by implementing straightforward and minimal processing endeavors. This method demonstrates significant efficiency in terms of complexity, cost, and energy consumption by utilizing a single-dimensional signal, eliminating the need for pre-processing steps, and limiting the features used for training.

</div>
</div>

- ``Biomedical Engineering: Applications, Basis and Communications. 2024`` [Effectiveness of Learning Rate in Dementia Severity Prediction Using VGG16](https://doi.org/10.4015/S1016237223500060), **Farhad Abedinzadeh Torghabeh**, Yeganeh Modaresnia, MOhammad Mahdi Khalilzadeh*.
- ``13th International Conference on Computer and Knowledge Engineering (ICCKE). 2023`` [An Efficient Approach for Breast Abnormality Detection through High-Level features of Thermography Images](https://doi.org/10.1109/ICCKE60553.2023.10326246), **Farhad Abedinzadeh Torghabeh**, Yeganeh Modaresnia, Seyyed Abed Hosseini*.
- ``13th International Conference on Computer and Knowledge Engineering (ICCKE). 2023`` [EfficientNetB0’s Hybrid Approach for Brain Tumor Classification from MRI Images Using Deep Learning and Bagging Trees](https://doi.org/10.1109/ICCKE60553.2023.10326290), Yeganeh Modaresnia, **Farhad Abedinzadeh Torghabeh**, Seyyed Abed Hosseini*.
- ``Iranian Journal of Medical Physics. 2023`` [Deep Learning-Based Brain Tumor Segmentation in MRI Images: A MobileNetV2-DeepLabv3+ Approach](https://doi.org/10.22038/ijmp.2023.73972.2313), **Farhad Abedinzadeh Torghabeh**, Seyyed Abed Hosseini*.


# 🎖 Honors and Awards
- *Islamic Azad University of Mashhad, Mashhad, Iran*, Ranked 2nd Among All Master Students of Biomedical Engineering, Department of Biomedical Engineering, Mashhad Branch, Islamic Azad University, Mashhad, Iran.
- *One Thousand Technological Ideas Tournament, Islamic Azad University of Mashhad, Mashhad, Iran*, Selected as a Finalist Among 100 Teams for Introducing the Concept of an Intelligent Ring for Epileptic Seizure Prediction Using HRV Signal.
- *Department of Biomedical Engineering, Mashhad Branch, Islamic Azad University, Mashhad, Iran*, Member of Biomedical Engineering Scientific Association.


# 📖 Educations
- *Jan 2021 - Aug 2023*, Master, Mashhad Branch, Islamic Azad University, Mashhad, Iran. M.Sc. of Biomedical Engineering, Sports Engineering. GPA: **17.40/20**.
- *Sep 2015 - Sep 2020*, Undergraduate, Sadjad University of Technology, Mashhad, Iran. 

# 💬 Research Experience
-``Academic Peer Reviewer``
- *Jan 2024 - Now*, Journal of Physical and Engineering Sciences in Medicine, Springer.
- *Sep 2023 - Now*, Journal of Computers in Biology and Medicine, Elsevier.
- *Jun 2023 - Now*, Journal of Pattern Recognition Letters, Elsevier.
- *Feb 2023 - Now*, Journal of Biomedical Signal Processing and Control, Elsevier.
-<br>``Undergraduate Research Assistant``
- *Oct 2021 - Now*, Under Assoc.Prof.Seyyed Abed Hosseini at the Islamic Azad University, Mashhad, Iran.
- Currently Working With on Several Research Projects, Including “Analysing Brain Connectivity Using Multimodality Data on Various Neurological Diseases”.

# 💻 Professional and Academic Experience
- *Jul 2022 - Oct 2022*, Instructor of  a Project-Oriented Course of Biomedical Image & Signal Processing Using MATLAB.
- *Jan 2022 - Now*, Freelance Programmer (Using MATLAB & Python) and Research Supervisor, On-site, Remote and Hybrid.

# 💻 CV
- [Download CV](files\cv\Farhad'sCV.pdf)