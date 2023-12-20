import streamlit as st
from re_gpt import SyncChatGPT

session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..lgmB4xvJuTtAQFrp.oEtxYqmuhGxlR40RUfpQxo460DGxk9C6QDqKVsjgeW6Xgn8vdRCNAg2lIXYXlyffbnARSD56Wb7tHRzUHcW-LsWtbytYgg5Alab6dhdq3PFYF8buXrmL0VKGUdUa9YSjoIfkDE0C5tNiinGbWK0l7X-46Vm9MWY0h4-KDiicF7UIpdiytVFhV3e6nNdX-Ai7tGwIit3ymD5t4C0AMSDhA9H7jWorvVWMVWp_EZj0oFa1Vu5WmTcMzW8skDBN0FUzpaTkWs9eJQHQ6AkAInZFHqz09yll3YO9--AtdMZFQyEvlgOM4BqS1VzbHsjbayv9Iy2f0wdupgEp-RqQMaVTtx0ncY3MK07krGC8g4wUALJD5Ns0spNsrR6sFyA8j9zi58H3tuSVfJgGTq2NQJamjtXdctc2Ujo_JP7Ko0hnr3mpJvs7oVLHcyixkqJLOYFhaqZC3tCvxSVREysZlzDcYE1IBTt19-Z9HPz5XHsg88Osv5LjB7BgAmk0A8gyd4EB_bexFIoANMel4mNZNZsICwtv9-2jImNOif3FNkTEkNRSxX0G-lVq7UHnjJO-V9YIgmba-1HT5sO9RMoBUX4MJecM9Ezq1Qx3NwGdlNOCo0jDw1Peu4thZs15KXqi8_a35EUHkHcMCj2FYUg1v51alwW4mgGuj2Jo-WocJL80-g9vzQwD4qdRjTFD9gbdGpeRzlgiGstk85hfiEhIVMEIpiw3hMTcYXLPE_oAEeuTGj72QSc0DPAYg1LIMleZgTYT4ehsK5dyGgWsHjYZ_Op8FS8vikfo_kzWmbBnEsfhdZTvwJvqlhYYWbb2zxFiilE2lPkbkQgakyZZx2IM51SYyyJZywVuwLJEvN4BNS_9_PxV8iYADONyosh_8jLT1b29F6j1-bOBC5u2pRny-QwY6Z8HLS2r4Suxy2If2FCxzg1OJ9Pz1PoXCtvzFCgTqHFIIWacGCYjIY59WHNLLPDYv55qxn3OehCPLAeC_MajuZqvWzP1iBWughczLK61yYiM_LOY9oKdALErwLWpsHtt56ED9E5Hv0JiFCjI6HAUCi67OR7jRcS8rFtsVvF7a-YOBY9rN7IlzfJXNtUGWe_NEnEOp49xigzede91iglICDMr7Tgm8nq1h9PSXz_OfBrfn5is55acMs-4nHGA1ya_6zI5NpiOdP6_iqseOMC7ArQ6Z_gigaHlTBy_jgQ1AkUt6XUDhTE6U_4ZN9zfab2qLcumXQUMbrvIpRk3V1Naxv8fv8AkfDWfNUVk0szPNyRDi3Ys1vNc0kaeI8fDzF5jNHt2OrFvL5NiltwytzNsHNl5x-3dJPUXElQ1fMnFqc8FbDAapZIGtrRxoS2XHxD8pIYc27lpm98kgnDR_IE1WY88ME608d_RcBOW07YAVPIy2E3YYlfkKNniOMoHX0I6gjM00PVVZJC7cR_6G9Lk65XUcqvor5E8J8erluKd8F5Fyq1D-24Ss8K46P1WECs7gKLgQhasGhyv8tmrBNeIuS02QFAgxwO_Gkj6xtwzgxZxMv6uYyn7H3vy_izaxr-ZftVWNkkCXsBdJFC-7SW8CPI8Z6Oi3a36rvay0ze2A70xJivinyDcDqyZKqBXPA-OudavtXWHoVUY07k5CqjgLU9gH2IgNNejB03C1QyXudFqJctZhkEQNpJR5lFq_NgoTdK_qk4elO4ROqNaLDU_0VXLkCszWcHh5qFjwrrGBWtcRePy-wyEc8qCp5yK-DOlGzSnRTFuUYaUmrxwJXr3FRcwmNvzpwgKVb9H2aGVch5CNEwuwoIwnlkZksvrFF-vf3PhF2Q8h2-_TgznMr1DuAzHia3ccwl-LM7DNoHqHSEjQVl7_dq65O7hj1X10itulOv8zZYyflv4kWx50oNdxn9QrVHdPKEhtDKz0O2ApLEHbP2l_VyrzbKBWyXkNVlnZnJTY5Bfo7huQ-R8cVLNO7rG3r8tbZjRxPHYUaAYKLcLHIi1R5urtYi9N2pt653i3FCh7MVDnXYvwtCLcOmyCAA02sWG5Hiv-NPkDrmjxngpBNv3xPoGv6TeeYWxoqbQvHlFnr-M5f0oYEH0kyq4ciWzqHOX3YZszUT0OrzUl7nQ7iVyzt1JIkm74dKWSQjiXnZVYJ9BYunJaZMWvF-MxlXBQ-Nfza9H0zjn5zuHd0ULrOtkaR3Oe0t5ta69m9FXpYoMI0cH_qb6A96MiyIqx90RGqX8Z-7OHtCCFetThUiALOnHSXQ84v6w9QYOvP-zzHF_6rfxjH6ISs8J1y6KRz53l82SDUux-CF5ezL9aZjsLkWeWYUnymldcNIgIxSyuY7Xq2bD8hpVtQTwhubAFhA3hL9CPycct4sSzFZIPg0b0dPchSaox5hX8_eEHM4gh0PhfrkWObIdnEkC27dqCdkK7zYXx6tsWrGagg_9bu4SY4NHEgYPRrI07k0RaSNPI757rW_7uYD-FmXSowdFsmsTK57kNHOr3Q2IbsERVABpG3qjzc-36sgWmWjedl3SiycGiCrkRS4zM3J7H6zWJY0tAIrdB6zdB5XCl6vAaggLoQyNx49sTPRi_0q540_8l56Fq1FqcX99pRy7Rz1D1q6Oo8mC-XcGtHJXBAhLfjWUznYwUblILf38d_Uh7PQmHsxjObLLlZtH8EnqDskd-qCzls32fWwp45A2wUA4h00ZgIxlc7DXulwOQoeerabxwquOmzPLhFLJIDW1tOH4jCnm1791x2Q8TbVvOheA4wvIWMuWiQYjKi5FByYEB_056UFp-zYItUlsHrgnPbEjkBnRhGUV2Xkp9TQrTgurn00Zzg.oxt7fJ1qRzcJtLe-USkt7g"
conversation_id = None  # Add your conversation ID here

def generate_questions(raw_text, learning_rate, num_questions):
    difficulty_levels = {
        0.5: "neutral",
        0.4: "layman's",
        0.6: "more complex and concise",
    }

    difficulty_level = difficulty_levels.get(learning_rate, "neutral")

    question_prompt = f"Ask {num_questions} questions about the following text:\n\n{raw_text}\n\nwith a {difficulty_level} difficulty level."

    with SyncChatGPT(session_token=session_token) as chatgpt:
        if conversation_id:
            conversation = chatgpt.get_conversation(conversation_id)
        else:
            conversation = chatgpt.create_new_conversation()

        response_text = ""
        for message in conversation.chat(question_prompt):
            response_text += message["content"]

        questions = response_text.split("\n")
        questions = [question.strip() for question in questions if question.strip()]

        return questions[:num_questions]

def verify_answers(questions_and_answers):
    verification_prompt = f"Check if the given answers are relevant for the following questions:\n\n{questions_and_answers}"

    #print(f"Verification Prompt: {verification_prompt}")  # Add this line for debugging

    with SyncChatGPT(session_token=session_token) as chatgpt:
        if conversation_id:
            conversation = chatgpt.get_conversation(conversation_id)
        else:
            conversation = chatgpt.create_new_conversation()

        verification_result = ""
        for message in conversation.chat(verification_prompt):
            verification_result += message["content"]

        return verification_result


def main():
    st.title("Viva Examiner with Learning Rate")
    raw_text = st.text_area("Enter raw text:")
    learning_rate = st.slider("Select Learning Rate", 0.0, 1.0, 0.5, 0.01)
    num_questions = st.slider("Select Number of Questions", 1, 10, 3)

    # Create a form
    with st.form("question_form"):
        generated_questions = generate_questions(raw_text, learning_rate, num_questions)

        st.subheader("Generated Questions:")
        st.write(generated_questions)

        answers_text = st.text_area("Enter answers with question numbers:")

        # Add a submit button within the form
        submitted = st.form_submit_button("Verify Answers")

        if submitted:
            #st.write("Verify Answers button clicked")  # For debugging
            #st.write(f"Verifying Answers for: {generated_questions} - {answers_text}")  # For debugging

            # Combine questions and answers into a single prompt
            questions_and_answers = "\n".join(f"{q}\nAnswer: {a}" for q, a in zip(generated_questions, answers_text.split('\n')))
            
            #st.write(f"Combined Questions and Answers:\n{questions_and_answers}")  # For debugging
            verification_result = verify_answers(questions_and_answers)

            st.subheader("Verification Result:")
            st.write(verification_result)


if __name__ == "__main__":
    main()
