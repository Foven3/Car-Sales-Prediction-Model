import gradio as gr
import joblib
import numpy as np

# Load scaler and model
scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

# Prediction function
def predict_car_price(age, salary, net_worth):
    # Scale input
    X_scaled = scaler.transform([[age, salary, net_worth]])
    # Predict
    prediction = model.predict(X_scaled)
    return f"${prediction[0]:,.2f}"

# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# 🚗 Customer Car Price Estimator")
    gr.Markdown(
        "Predict a customer's car purchase amount based on their **age**, **annual salary**, and **net worth**. "
        "This tool helps businesses understand potential spending and offer better recommendations."
    )

    with gr.Row():
        with gr.Column():
            age_input = gr.Number(label="Age", value=40, precision=0, minimum=18, maximum=90)
            salary_input = gr.Number(label="Annual Salary ($)", value=30000, step=1000, minimum=1000)
            networth_input = gr.Number(label="Net Worth ($)", value=100000, step=5000, minimum=0)
            predict_btn = gr.Button("Calculate Price")

        with gr.Column():
            output = gr.Textbox(label="Predicted Car Purchase Amount")

    predict_btn.click(
        fn=predict_car_price,
        inputs=[age_input, salary_input, networth_input],
        outputs=output
    )

# Launch app
demo.launch(share=True)
