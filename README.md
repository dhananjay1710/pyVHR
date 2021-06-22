

---

## Description
This Repository is a modified version of the PyVHR repository proposed in https://github.com/phuselab/pyVHR, combined with the toolkit HeartPy https://python-heart-rate-analysis-toolkit.readthedocs.io/en/latest/ , and the open source code for Spo2 https://github.com/CoVital-Project/Spo2_evaluation. This project aims to extract 3 vital signs (HH, BR and Spo2) from a video.

**Package pyVHR** (short for Python framework for Virtual Heart Rate) is a comprehensive framework for studying methods of pulse rate estimation relying on remote photoplethysmography (rPPG). The methodological rationale behind the framework is that in order to study, develop and compare new rPPG methods in a principled and reproducible way, the following conditions should be met: *i)* a structured pipeline to monitor rPPG algorithms' input, output, and main control parameters; *ii)* the availability and the use of multiple datasets; *iii)* a sound statistical assessment of methods' performance.
pyVHR allows to easily handle rPPGmethods  and  data,  while  simplifying  the  statistical  assessment. Its main features lie in the following.
- **Analysis-oriented**. It  constitutes  a  platform  for  experiment design, involving an arbitrary number of methods applied to multiple video datasets. It provides a systemic end-to-end  pipeline,  allowing  to  assess  different  rPPG  algorithms, by easily setting parameters and meta-parameters.
- **Openness**. It comprises both method and dataset factory, so to easily extend the pool of elements to be evaluatedwith newly developed rPPG methods and any kind of videodatasets.
- **Robust assessment**. The outcomes are arranged intostructured data ready for in-depth analyses. Performance comparison is carried out based on robust nonparametric statistical tests.

Eight well-known rPPG methods, namely  *ICA*,  *PCA*, *GREEN,CHROM*, *POS*, *SSR*, *LGI*, *PBV*, are evaluated through extensive experiments across five public video datasets,  i.e. *PURE*, *LGI*, *USBC*, *MAHNOB* and *COHFACE*, and subsequent nonparametric statistical analysis.  

![pyVHR](https://raw.githubusercontent.com/phuselab/pyVHR/master/img/frameworkVHR.png)

## Installation

Install the dependency:

```text
$ apt-get install cmake gfortran
$ pip install numpy
$`pip install opencv-python
$ pip install matplotlib
$ pip install heartpy

Do not instal the pyVHR library directly due to this project has modified the original one.
```
```

## Usage
*Use short videos (.mp4 or .avi) 
*If you want to record a video using your pc camera, run the video-record.py file to capture a short video (10 sec)
*Run the test1.py file to extract the Hearth Rate, the Breath Reate and the Oxigen Saturation from the video (modify the script with the correponding video filepath)



## Methods

The framework contains the implementation of the most common methods for remote-PPG measurement, and are located in the `methods` folder.  
Currently implemented methods with reference publications are:

**Green**
> Verkruysse, W., Svaasand, L. O., & Nelson, J. S. (2008). Remote plethysmographic imaging using ambient light. Optics express, 16(26), 21434-21445.

**CHROM**
> De Haan, G., & Jeanne, V. (2013). Robust pulse rate from chrominance-based rPPG. IEEE Transactions on Biomedical Engineering, 60(10), 2878-2886.

**ICA**
> Poh, M. Z., McDuff, D. J., & Picard, R. W. (2010). Non-contact, automated cardiac pulse measurements using video imaging and blind source separation. Optics express, 18(10), 10762-10774.

**LGI**
> Pilz, C. S., Zaunseder, S., Krajewski, J., & Blazek, V. (2018). Local group invariance for heart rate estimation from face videos in the wild. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition Workshops (pp. 1254-1262).

**PBV**
> De Haan, G., & Van Leest, A. (2014). Improved motion robustness of remote-PPG by using the blood volume pulse signature. Physiological measurement, 35(9), 1913.

**PCA**
> Lewandowska, M., Rumiński, J., Kocejko, T., & Nowak, J. (2011, September). Measuring pulse rate with a webcam—a non-contact method for evaluating cardiac activity. In 2011 federated conference on computer science and information systems (FedCSIS) (pp. 405-410). IEEE.

**POS** These was the method used in the main file, due to the state of the art suggested as the robust one
> Wang, W., den Brinker, A. C., Stuijk, S., & de Haan, G. (2016). Algorithmic principles of remote PPG. IEEE Transactions on Biomedical Engineering, 64(7), 1479-1491.

**SSR**
> Wang, W., Stuijk, S., & De Haan, G. (2015). A novel algorithm for remote photoplethysmography: Spatial subspace rotation. IEEE transactions on biomedical engineering, 63(9), 1974-1984.

SPO2 method:
Lamonaca, F., Carnì, D. L., Grimaldi, D., Nastro, A., Riccio, M., & Spagnolo, V. (2015, May). Blood oxygen saturation measurement by smartphone camera. In 2015 IEEE International Symposium on Medical Measurements and Applications (MeMeA) Proceedings (pp. 359-364). IEEE.


## Reference

G. Boccignone, D. Conte, V. Cuculo, A. D’Amelio, G. Grossi and R. Lanzarotti, "An Open Framework for Remote-PPG Methods and their Assessment," in *IEEE Access*, doi: [10.1109/ACCESS.2020.3040936](https://ieeexplore.ieee.org/document/9272290).

To cite the original paper of pyVHR from pulseLab:

```
@article{pyVHR2020,
  doi = {10.1109/access.2020.3040936},
  url = {https://doi.org/10.1109/access.2020.3040936},
  year = {2020},
  publisher = {Institute of Electrical and Electronics Engineers ({IEEE})},
  pages = {1--1},
  author = {Giuseppe Boccignone and Donatello Conte and Vittorio Cuculo and Alessandro D’Amelio and Giuliano Grossi and Raffaella Lanzarotti},
  title = {An Open Framework for Remote-{PPG} Methods and their Assessment},
  journal = {{IEEE} Access}
}
```

## License

The original project pyVHR is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details
