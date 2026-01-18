import streamlit as st
from bank import Bank

bank = Bank()

st.set_page_config(page_title="Mini Bank System", layout="centered")
st.title("🏦 roman hero ko hai Bank System")

menu = st.sidebar.selectbox(
    "Choose Action",
    ["Create Account", "Deposit", "Withdraw", "View Details", "Delete Account"]
)

# ---------- CREATE ACCOUNT ----------
if menu == "Create Account":
    st.subheader("Create Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    pin = st.text_input("PIN (4 digits)", type="password")

    if st.button("Create"):
        success, result = bank.create_account(name, age, email, int(pin))
        if success:
            st.success("Account Created!")
            st.write("Account Number:", result["accountno"])
        else:
            st.error(result)

# ---------- DEPOSIT ----------
elif menu == "Deposit":
    st.subheader("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=0)

    if st.button("Deposit"):
        success, msg = bank.deposit(acc, int(pin), amount)
        st.success(f"New Balance: {msg}") if success else st.error(msg)

# ---------- WITHDRAW ----------
elif menu == "Withdraw":
    st.subheader("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=0)

    if st.button("Withdraw"):
        success, msg = bank.withdraw(acc, int(pin), amount)
        st.success(f"Remaining Balance: {msg}") if success else st.error(msg)

# ---------- VIEW DETAILS ----------
elif menu == "View Details":
    st.subheader("Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("View"):
        user = bank.find_user(acc, int(pin))
        if user:
            for k, v in user.items():
                if k != "pin":
                    st.write(f"**{k}**: {v}")
        else:
            st.error("Invalid credentials")

# ---------- DELETE ACCOUNT ----------
elif menu == "Delete Account":
    st.subheader("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        success, msg = bank.delete_account(acc, int(pin))
        st.success(msg) if success else st.error(msg)
