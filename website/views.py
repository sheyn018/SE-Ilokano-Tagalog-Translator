import pandas as pd
from flask import Blueprint, render_template, request
from module.tl_il.doc_trans_smt_tl import tl_smt_trans
from module.il_tl.doc_trans_smt_il import il_smt_trans

views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
def home():
    """
    Route for the home page of the application
    """
    return render_template("index.html")

@views.route('/il_tag', methods=['GET', 'POST'])
def il_tag():
    """
    Route for the page that handles the Ilokano to Tagalog machine translation
    """
    source = ''
    op_sen_list = []
    if request.method == 'POST':
        source = request.form.get('source_lang')
        dict_il_tl_result = il_smt_trans(source)
        dict_il_tl_result = pd.DataFrame(dict_il_tl_result)
        op_sen_list = dict_il_tl_result['System Output'].tolist()
    
    return render_template('il-tg_translator.html', source=source, op_sen_list=op_sen_list)

@views.route('/tag_il', methods=['GET', 'POST'])
def tag_il():
    """
    Route for the page that handles the Tagalog to Ilokano machine translation
    """
    source = ''
    op_sen_list = []
    if request.method == 'POST':
        source = request.form.get('source_lang')
        dict_tl_il_result = tl_smt_trans(source)
        dict_tl_il_result = pd.DataFrame(dict_tl_il_result)
        op_sen_list = dict_tl_il_result['System Output'].tolist()
    
    return render_template('tg-il_translator.html', source=source, op_sen_list=op_sen_list)

@views.route('/system_tester_tg_il')
def system_tester_tg_il():
    """
    Route for the page that handles the system tester for Tagalog to Ilokano machine translation
    """
    return render_template('system_tester_tg-il.html')

@views.route('/system_tester_il_tg')
def system_tester_il_tg():
    """
    Route for the page that handles the system tester for Ilokano to Tagalog machine translation
    """
    return render_template('system_tester_il-tg.html')