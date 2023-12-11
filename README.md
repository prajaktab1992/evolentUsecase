#####  evolentUsecase

Trained model should be saved under "outputs" folder

create new python conda enviornment
conda create --name llmfinetune
conda activate llmfinetune
pip install -r requirements.txt 

Train model
Model finetunning code notebook : FlanT5_classification_llmfinetunning.py Colab notebook

Make sure after training outputs folder should be available to below code to run and predict.
Endpoint application  code: textclassification_main.py
python textclassification_main.py

Endpoint : localhost:5000/predict


Input format :
{
    "medical_text":"Catheterization laboratory events and hospital outcome with direct angioplasty for acute myocardial infarction To assess the safety of direct infarct angioplasty without antecedent thrombolytic therapy, catheterization laboratory and hospital events were assessed in consecutively treated patients with infarctions involving the left anterior descending (n = 100 patients), right (n = 100), and circumflex (n = 50) coronary arteries. The groups of patients were similar for age (left anterior descending coronary artery, 59 years; right coronary artery, 58 years; circumflex coronary artery, 62 years), patients with multivessel disease (left anterior descending coronary artery, 55%; right coronary artery, 55%; circumflex coronary artery, 64%), and patients with initial grade 0/1 antegrade flow (left anterior descending coronary artery, 79%; right coronary artery, 84%; circumflex coronary artery, 90%). Cardiogenic shock was present in eight patients with infarction of the left anterior descending coronary artery, four with infarction of the right coronary artery, and four with infarction of the circumflex coronary artery. Major catheterization laboratory events (cardioversion, cardiopulmonary resuscitation, dopamine or intra-aortic balloon pump support for hypotension, and urgent surgery) occurred in 10 patients with infarction of the left anterior descending coronary artery, eight with infarction of the right coronary artery, and four with infarction of the circumflex coronary artery (16 of 16 shock and six of 234 nonshock patients, p less than 0.001). There was one in-laboratory death (shock patient with infarction of the left anterior descending coronary artery). "
}



output format:
{
    "Category": "4",
    "Description": "nervous system disease",
    "medical text": "Catheterization laboratory events and hospital outcome with direct angioplasty for acute myocardial infarction To assess the safety of direct infarct angioplasty without antecedent thrombolytic therapy, catheterization laboratory and hospital events were assessed in consecutively treated patients with infarctions involving the left anterior descending (n = 100 patients), right (n = 100), and circumflex (n = 50) coronary arteries. The groups of patients were similar for age (left anterior descending coronary artery, 59 years; right coronary artery, 58 years; circumflex coronary artery, 62 years), patients with multivessel disease (left anterior descending coronary artery, 55%; right coronary artery, 55%; circumflex coronary artery, 64%), and patients with initial grade 0/1 antegrade flow (left anterior descending coronary artery, 79%; right coronary artery, 84%; circumflex coronary artery, 90%). Cardiogenic shock was present in eight patients with infarction of the left anterior descending coronary artery, four with infarction of the right coronary artery, and four with infarction of the circumflex coronary artery. Major catheterization laboratory events (cardioversion, cardiopulmonary resuscitation, dopamine or intra-aortic balloon pump support for hypotension, and urgent surgery) occurred in 10 patients with infarction of the left anterior descending coronary artery, eight with infarction of the right coronary artery, and four with infarction of the circumflex coronary artery (16 of 16 shock and six of 234 nonshock patients, p less than 0.001). There was one in-laboratory death (shock patient with infarction of the left anterior descending coronary artery). "
}
