import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="Al-Shalawi Company for Gold & Jewellery - Odoo.sh Setup Guide", layout="centered")

# Language Selection
language = st.sidebar.selectbox("Select Language / اختر اللغة", ["English", "العربية"])

# RTL for Arabic
def rtl_style():
    st.markdown(
        """
        <style>
        body {
            direction: rtl;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

if language == "العربية":
    rtl_style()

# Content in English or Arabic
if language == "English":
    # Title and Introduction
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 20px;">
            <h1 style="color: #2E86C1;">Al-Shalawi Company for Gold & Jewellery</h1>
            <h2 style="color: #34495E;">Your Odoo.sh Setup Guide</h2>
            <p style="font-size: 18px;">We have set up all the necessary accounts and configurations for you. Use the links below to access your accounts and manage your Odoo.sh database.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Company Information
    st.markdown(
        """
        <div style="background-color: #F8F9F9; padding: 20px; border-radius: 10px; border: 2px solid #2E86C1;">
            <h3 style="color: #2C3E50;">Company Profile</h3>
            <p><strong>Al-Shalawi Company for Gold & Jewellery</strong></p>
            <p>11484 Riyadh</p>
            <p>Saudi Arabia</p>
            <p>Phone: +966 50 891 4929</p>
            <p>Email: <a href="mailto:a.elbarbary@al-shalawi.com.sa">a.elbarbary@al-shalawi.com.sa</a></p>
            <p>URL: <a href="https://elsalwa-gold.odoo.com" target="_blank">https://elsalwa-gold.odoo.com</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Step 1: Access Your Google Account
    st.markdown(
        """
        <div style="margin-top: 20px; border: 2px solid #2E86C1; padding: 20px; border-radius: 10px;">
            <h3 style="color: #2E86C1;">1. Access Your Google Account</h3>
            <p>Click the button below to log in to your Google account using the credentials we provided (Email: elsalwagold@gmail.com).</p>
            <a href="https://accounts.google.com/" target="_blank" style="text-decoration: none;">
                <button style="background-color: #2E86C1; color: white; padding: 10px 20px; border: none; border-radius: 5px;">Login to Google Account</button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Step 2: Access Your GitHub Account
    st.markdown(
        """
        <div style="margin-top: 20px; border: 2px solid #2E86C1; padding: 20px; border-radius: 10px;">
            <h3 style="color: #2E86C1;">2. Access Your GitHub Account</h3>
            <p>Click the button below to log in to your GitHub account. Use the Google account (elsalwagold@gmail.com) to sign in.</p>
            <a href="https://github.com/login" target="_blank" style="text-decoration: none;">
                <button style="background-color: #2E86C1; color: white; padding: 10px 20px; border: none; border-radius: 5px;">Login to GitHub Account</button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Step 3: Access Your Odoo.sh Account
    st.markdown(
        """
        <div style="margin-top: 20px; border: 2px solid #2E86C1; padding: 20px; border-radius: 10px;">
            <h3 style="color: #2E86C1;">3. Access Your Odoo.sh Account</h3>
            <p>Click the button below to log in to your Odoo.sh account. Make sure you are already logged into your GitHub account in the same browser before accessing Odoo.sh.</p>
            <a href="https://www.odoo.sh" target="_blank" style="text-decoration: none;">
                <button style="background-color: #2E86C1; color: white; padding: 10px 20px; border: none; border-radius: 5px;">Login to Odoo.sh Account</button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Step 4: Pre-installed and Configured Applications
    st.markdown(
        """
        <div style="margin-top: 20px; border: 2px solid #2E86C1; padding: 20px; border-radius: 10px;">
            <h3 style="color: #2E86C1;">4. Pre-installed and Configured Applications</h3>
            <p>The following applications have been pre-installed and configured in your Odoo.sh database:</p>
            <ul style="line-height: 1.8;">
                <li><strong>Sales (sale_management)</strong>: Manage your sales orders and quotations efficiently.</li>
                <li><strong>Invoicing (account)</strong>: Handle your financial operations, including invoices and payments.</li>
                <li><strong>Inventory (stock)</strong>: Track your stock levels, incoming shipments, and deliveries.</li>
                <li><strong>Accounting (accountant)</strong>: Comprehensive accounting management features.</li>
                <li><strong>Purchase (purchase)</strong>: Streamline your procurement process with purchase orders.</li>
                <li><strong>Time Off (hr_holidays)</strong>: Manage employee leaves and time-off requests.</li>
                <li><strong>Employees (hr)</strong>: Maintain employee records and HR information.</li>
                <li><strong>Discuss (mail)</strong>: Centralized communication platform for internal discussions.</li>
                <li><strong>Contacts (contacts)</strong>: Organize and manage all your business contacts.</li>
                <li><strong>Calendar (calendar)</strong>: Schedule and manage meetings and events.</li>
                <li><strong>Attendances (hr_attendance)</strong>: Track employee attendance and working hours.</li>
                <li><strong>Skills Management (hr_skills)</strong>: Manage employee skills and competencies.</li>
                <li><strong>Payroll (hr_payroll)</strong>: Handle employee salaries and payroll processing.</li>
                <li><strong>Employee Contracts (hr_contract)</strong>: Manage employment contracts and agreements.</li>
                <li><strong>Barcode (stock_barcode)</strong>: Utilize barcode scanning for inventory management.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Step 5: Manage Your Odoo.sh Database
    st.markdown(
        """
        <div style="margin-top: 20px; border: 2px solid #2E86C1; padding: 20px; border-radius: 10px;">
            <h3 style="color: #2E86C1;">5. Manage Your Odoo.sh Database</h3>
            <p>We have created and configured your Odoo.sh database. Here’s how to activate and manage it:</p>
            <ol style="line-height: 1.8;">
                <li>Log in to your Odoo.sh account using the link above.</li>
                <li>Select your project and open the database.</li>
                <li>Navigate to <strong>Settings > Subscription</strong>.</li>
                <li>The subscription code has already been applied. You can start using your database immediately.</li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Note on Support
    st.markdown(
        """
        <div style="background-color: #F8F9F9; padding: 20px; margin-top: 20px; border-radius: 10px; border: 2px solid #2E86C1;">
            <h3 style="color: #2C3E50;">Need Assistance?</h3>
            <p>If you encounter any issues, please contact our support team at <a href="mailto:a.elbarbary@al-shalawi.com.sa">a.elbarbary@al-shalawi.com.sa</a>. We’re here to help!</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Footer
    st.markdown(
        """
        <hr style="margin-top: 20px;">
        <p style="text-align: center; color: #7B7D7D;">Developed by Al-Shalawi Company for Gold & Jewellery</p>
        """,
        unsafe_allow_html=True
    )

else:
    # Arabic Content
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 20px;">
            <h1 style="color: #2E86C1;">شركة الشلوي للذهب والمجوهرات</h1>
            <h2 style="color: #34495E;">دليل إعداد Odoo.sh الخاص بك</h2>
            <p style="font-size: 18px;">لقد قمنا بإعداد جميع الحسابات والتكوينات اللازمة لك. استخدم الروابط أدناه للوصول إلى حساباتك وإدارة قاعدة بيانات Odoo.sh الخاصة بك.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Arabic Content for Company Profile
    st.markdown(
        """
        <div style="background-color: #F8F9F9; padding: 20px; border-radius: 10px; border: 2px solid #2E86C1;">
            <h3 style="color: #2C3E50;">معلومات الشركة</h3>
            <p><strong>شركة الشلوي للذهب والمجوهرات</strong></p>
            <p>11484 الرياض</p>
            <p>المملكة العربية السعودية</p>
            <p>الهاتف: +966 50 891 4929</p>
            <p>البريد الإلكتروني: <a href="mailto:a.elbarbary@al-shalawi.com.sa">a.elbarbary@al-shalawi.com.sa</a></p>
            <p>رابط الموقع: <a href="https://elsalwa-gold.odoo.com" target="_blank">https://elsalwa-gold.odoo.com</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Step 1: Access Your Google Account
    st.markdown(
        """
        <div style="margin-top: 20px; border: 2px solid #2E86C1; padding: 20px; border-radius: 10px;">
            <h3 style="color: #2E86C1;">1. الوصول إلى حساب Google الخاص بك</h3>
            <p>اضغط على الزر أدناه لتسجيل الدخول إلى حساب Google الخاص بك باستخدام بيانات الاعتماد التي قدمناها لك (البريد الإلكتروني: elsalwagold@gmail.com).</p>
            <a href="https://accounts.google.com/" target="_blank" style="text-decoration: none;">
                <button style="background-color: #2E86C1; color: white; padding: 10px 20px; border: none; border-radius: 5px;">تسجيل الدخول إلى حساب Google</button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Step 2: Access Your GitHub Account
    st.markdown(
        """
        <div style="margin-top: 20px; border: 2px solid #2E86C1; padding: 20px; border-radius: 10px;">
            <h3 style="color: #2E86C1;">2. الوصول إلى حساب GitHub الخاص بك</h3>
            <p>اضغط على الزر أدناه لتسجيل الدخول إلى حساب GitHub الخاص بك. استخدم حساب Google (elsalwagold@gmail.com) لتسجيل الدخول.</p>
            <a href="https://github.com/login" target="_blank" style="text-decoration: none;">
                <button style="background-color: #2E86C1; color: white; padding: 10px 20px; border: none; border-radius: 5px;">تسجيل الدخول إلى حساب GitHub</button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Step 3: Access Your Odoo.sh Account
    st.markdown(
        """
        <div style="margin-top: 20px; border: 2px solid #2E86C1; padding: 20px; border-radius: 10px;">
            <h3 style="color: #2E86C1;">3. الوصول إلى حساب Odoo.sh الخاص بك</h3>
            <p>اضغط على الزر أدناه لتسجيل الدخول إلى حساب Odoo.sh الخاص بك. تأكد من تسجيل الدخول بالفعل إلى حساب GitHub الخاص بك في نفس المتصفح قبل الوصول إلى Odoo.sh.</p>
            <a href="https://www.odoo.sh" target="_blank" style="text-decoration: none;">
                <button style="background-color: #2E86C1; color: white; padding: 10px 20px; border: none; border-radius: 5px;">تسجيل الدخول إلى حساب Odoo.sh</button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Step 4: Pre-installed and Configured Applications
    st.markdown(
        """
        <div style="margin-top: 20px; border: 2px solid #2E86C1; padding: 20px; border-radius: 10px;">
            <h3 style="color: #2E86C1;">4. التطبيقات المثبتة والمهيأة مسبقًا</h3>
            <p>تم تثبيت وتهيئة التطبيقات التالية مسبقًا في قاعدة بيانات Odoo.sh الخاصة بك:</p>
            <ul style="line-height: 1.8;">
                <li><strong>المبيعات (sale_management)</strong>: إدارة طلبات المبيعات والعروض بكفاءة.</li>
                <li><strong>الفوترة (account)</strong>: التعامل مع العمليات المالية بما في ذلك الفواتير والمدفوعات.</li>
                <li><strong>المخزون (stock)</strong>: تتبع مستويات المخزون والشحنات الواردة والتسليمات.</li>
                <li><strong>المحاسبة (accountant)</strong>: ميزات شاملة لإدارة المحاسبة.</li>
                <li><strong>المشتريات (purchase)</strong>: تبسيط عملية المشتريات من خلال أوامر الشراء.</li>
                <li><strong>الإجازات (hr_holidays)</strong>: إدارة إجازات الموظفين وطلبات الإجازة.</li>
                <li><strong>الموظفين (hr)</strong>: حفظ سجلات الموظفين ومعلومات الموارد البشرية.</li>
                <li><strong>الدردشة (mail)</strong>: منصة اتصال مركزية للنقاشات الداخلية.</li>
                <li><strong>جهات الاتصال (contacts)</strong>: تنظيم وإدارة جميع جهات الاتصال الخاصة بالعمل.</li>
                <li><strong>التقويم (calendar)</strong>: جدولة وإدارة الاجتماعات والفعاليات.</li>
                <li><strong>الحضور (hr_attendance)</strong>: تتبع حضور الموظفين وساعات العمل.</li>
                <li><strong>إدارة المهارات (hr_skills)</strong>: إدارة مهارات الموظفين وكفاءاتهم.</li>
                <li><strong>الرواتب (hr_payroll)</strong>: التعامل مع رواتب الموظفين ومعالجة الرواتب.</li>
                <li><strong>عقود الموظفين (hr_contract)</strong>: إدارة عقود واتفاقيات العمل.</li>
                <li><strong>الباركود (stock_barcode)</strong>: استخدام مسح الباركود لإدارة المخزون.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Step 5: Manage Your Odoo.sh Database
    st.markdown(
        """
        <div style="margin-top: 20px; border: 2px solid #2E86C1; padding: 20px; border-radius: 10px;">
            <h3 style="color: #2E86C1;">5. إدارة قاعدة بيانات Odoo.sh الخاصة بك</h3>
            <p>لقد قمنا بإنشاء وتكوين قاعدة بيانات Odoo.sh الخاصة بك. إليك كيفية تنشيطها وإدارتها:</p>
            <ol style="line-height: 1.8;">
                <li>قم بتسجيل الدخول إلى حساب Odoo.sh الخاص بك باستخدام الرابط أعلاه.</li>
                <li>اختر مشروعك وافتح قاعدة البيانات.</li>
                <li>انتقل إلى <strong>الإعدادات > الاشتراك</strong>.</li>
                <li>تم تطبيق رمز الاشتراك بالفعل. يمكنك البدء في استخدام قاعدة البيانات الخاصة بك على الفور.</li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Note on Support
    st.markdown(
        """
        <div style="background-color: #F8F9F9; padding: 20px; margin-top: 20px; border-radius: 10px; border: 2px solid #2E86C1;">
            <h3 style="color: #2C3E50;">هل تحتاج إلى مساعدة؟</h3>
            <p>إذا واجهت أي مشاكل، يرجى الاتصال بفريق الدعم لدينا على <a href="mailto:a.elbarbary@al-shalawi.com.sa">a.elbarbary@al-shalawi.com.sa</a>. نحن هنا لمساعدتك!</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Footer
    st.markdown(
        """
        <hr style="margin-top: 20px;">
        <p style="text-align: center; color: #7B7D7D;">تم التطوير بواسطة شركة الشلاوي للذهب والمجوهرات</p>
        """,
        unsafe_allow_html=True
    )
