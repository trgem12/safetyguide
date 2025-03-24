from flask import Flask, render_template, send_from_directory

import os, re

app = Flask(__name__)

@app.route("/")  # 127.0.0.1
def index():
    # 'templates' 폴더에서 'index.html' 템플릿을 렌더링합니다.
    return render_template("index.html")

@app.route("/<string:page_name>.html")  # 다른 HTML 페이지에 대한 동적 라우트
def show_page(page_name):
    return render_template(f"{page_name}.html")


@app.route("/safetygear.html")
def safetygear():
    image_folder = os.path.join(app.static_folder, 'assets/안전보호구safetygear')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('safetygear.html', images=image_files)

@app.route("/riskassessment.html")
def riskassessment():
    image_folder = os.path.join(app.static_folder, 'assets/위험성평가riskassessment')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('riskassessment.html', images=image_files)

@app.route("/tbm.html")
def tbm():
    image_folder = os.path.join(app.static_folder, 'assets/tbm')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('tbm.html', images=image_files)

@app.route("/workplan.html")
def workplan():
    image_folder = os.path.join(app.static_folder, 'assets/작업계획서workplan')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('workplan.html', images=image_files)

@app.route("/ladder.html")
def ladder():
    image_folder = os.path.join(app.static_folder, 'assets/사다리고소작업대ladder')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('ladder.html', images=image_files)

@app.route("/electricity.html")
def electricity():
    image_folder = os.path.join(app.static_folder, 'assets/전원(전기)electricity')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('electricity.html', images=image_files)

@app.route("/roadside.html")
def roadside():
    image_folder = os.path.join(app.static_folder, 'assets/도로변작업(신호수)roadside')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('roadside.html', images=image_files)

@app.route("/confinedspace.html")
def confinedspace():
    image_folder = os.path.join(app.static_folder, 'assets/밀폐공간confinedspace')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('confinedspace.html', images=image_files)

@app.route("/temperatures.html")
def temperatures():
    image_folder = os.path.join(app.static_folder, 'assets/기온temperatures')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('temperatures.html', images=image_files)

@app.route("/sanctionstandards.html")
def sanctionstandards():
    image_folder = os.path.join(app.static_folder, 'assets/기타(sgr제재기준)sanctionstandards')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('sanctionstandards.html', images=image_files)

@app.route("/response.html")
def response():
    image_folder = os.path.join(app.static_folder, 'assets/산업중대재해대응response')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('response.html', images=image_files)

@app.route("/responsesystem.html")
def responsesystem():
    image_folder = os.path.join(app.static_folder, 'assets/중대재해대응체계responsesystem')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('responsesystem.html', images=image_files)

@app.route("/responseguide.html")
def responseguide():
    image_folder = os.path.join(app.static_folder, 'assets/중대재해대응가이드responseguide')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('responseguide.html', images=image_files)

@app.route("/mocktraining.html")
def mocktraining():
    image_folder = os.path.join(app.static_folder, 'assets/중대재해모의훈련mocktraining')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('mocktraining.html', images=image_files)

@app.route("/contact.html")
def contact():
    image_folder = os.path.join(app.static_folder, 'assets/전국지방고용노동관서contact')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('contact.html', images=image_files)

@app.route("/questionnaire.html")
def questionnaire():
    image_folder = os.path.join(app.static_folder, 'assets/산업재해 조사표questionnaire')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('questionnaire.html', images=image_files)

@app.route("/cspo.html")
def cspo():
    image_folder = os.path.join(app.static_folder, 'assets/cspo인사말')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('cspo.html', images=image_files)

@app.route("/managementpolicy.html")
def managementpolicy():
    image_folder = os.path.join(app.static_folder, 'assets/경영방침managementpolicy')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('managementpolicy.html', images=image_files)
@app.route("/rolebyjob.html")
def rolebyjob():
    image_folder = os.path.join(app.static_folder, 'assets/직무별열할rolebyjob')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('rolebyjob.html', images=image_files)

@app.route("/sgr.html")
def sgr():
    image_folder = os.path.join(app.static_folder, 'assets/sgr')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('sgr.html', images=image_files)

@app.route("/safetylevel.html")
def safetylevel():
    image_folder = os.path.join(app.static_folder, 'assets/안전등급safetylevel')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('safetylevel.html', images=image_files)

@app.route("/workplan2.html")
def workplan2():
    image_folder = os.path.join(app.static_folder, 'assets/작업계획서특별교육workplan2')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('workplan2.html', images=image_files)

@app.route("/highriskwork.html")
def highriskwork():
    image_folder = os.path.join(app.static_folder, 'assets/고위험작업입회highriskwork')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('highriskwork.html', images=image_files)

@app.route("/twopeople.html")
def twopeople():
    image_folder = os.path.join(app.static_folder, 'assets/2인1조twopeople')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('twopeople.html', images=image_files)

@app.route("/tbm2.html")
def tbm2():
    image_folder = os.path.join(app.static_folder, 'assets/tbm2')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('tbm2.html', images=image_files)

@app.route("/safetyaccidents.html")
def safetyaccidents():
    image_folder = os.path.join(app.static_folder, 'assets/안전사고보고체계safetyaccidents')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('safetyaccidents.html', images=image_files)

@app.route("/aerialwork.html")
def aerialwork():
    image_folder = os.path.join(app.static_folder, 'assets/고소작업대aerialwork')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('aerialwork.html', images=image_files)

@app.route("/mobilecrane.html")
def mobilecrane():
    image_folder = os.path.join(app.static_folder, 'assets/이동식크레인mobilecrane')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('mobilecrane.html', images=image_files)

@app.route("/forklift.html")
def forklift():
    image_folder = os.path.join(app.static_folder, 'assets/지게차forklift')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('forklift.html', images=image_files)

@app.route("/excavator.html")
def excavator():
    image_folder = os.path.join(app.static_folder, 'assets/굴착기excavator')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('excavator.html', images=image_files)

@app.route("/truck.html")
def truck():
    image_folder = os.path.join(app.static_folder, 'assets/트럭류truck')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('truck.html', images=image_files)

@app.route("/portableladder.html")
def portableladder():
    image_folder = os.path.join(app.static_folder, 'assets/이동식사다리portableladder')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('portableladder.html', images=image_files)

@app.route("/safetybelt.html")
def safetybelt():
    image_folder = os.path.join(app.static_folder, 'assets/이동식사다리safetybelt')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('safetybelt.html', images=image_files)

@app.route("/scaffolding.html")
def scaffolding():
    image_folder = os.path.join(app.static_folder, 'assets/비계(이동식비계)scaffolding')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('scaffolding.html', images=image_files)

@app.route("/electricalwork.html")
def electricalwork():
    image_folder = os.path.join(app.static_folder, 'assets/전기작업안전electricalwork')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('electricalwork.html', images=image_files)

@app.route("/hotwork.html")
def hotwork():
    image_folder = os.path.join(app.static_folder, 'assets/화기작업안전hotwork')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('hotwork.html', images=image_files)

@app.route("/roadsidework.html")
def roadsidework():
    image_folder = os.path.join(app.static_folder, 'assets/도로변작업roadsidework')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('roadsidework.html', images=image_files)

@app.route("/confinedspacework.html")
def confinedspacework():
    image_folder = os.path.join(app.static_folder, 'assets/밀폐공간작업confinedspacework')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('confinedspacework.html', images=image_files)

@app.route("/heavywork.html")
def heavywork():
    image_folder = os.path.join(app.static_folder, 'assets/중량물작업heavywork')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('heavywork.html', images=image_files)

@app.route("/safetygear2.html")
def safetygear2():
    image_folder = os.path.join(app.static_folder, 'assets/안전보호구(kcs)safetygear2')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('safetygear2.html', images=image_files)

@app.route("/seasonalresponse.html")
def seasonalresponse():
    image_folder = os.path.join(app.static_folder, 'assets/계절별대응seasonalresponse')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('seasonalresponse.html', images=image_files)

@app.route("/emergencymeasures.html")
def emergencymeasures():
    image_folder = os.path.join(app.static_folder, 'assets/응급조치emergencymeasures')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('emergencymeasures.html', images=image_files)

@app.route("/worknstructions.html")
def worknstructions():
    image_folder = os.path.join(app.static_folder, 'assets/전송 현장 작업지침서 목차 work nstructions')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('worknstructions.html', images=image_files)

@app.route("/tbm3.html")
def tbm3():
    image_folder = os.path.join(app.static_folder, 'assets/tbm3')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('tbm3.html', images=image_files)

@app.route("/safetystandards.html")
def safetystandards():
    image_folder = os.path.join(app.static_folder, 'assets/안전기준safetystandards')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('safetystandards.html', images=image_files)

@app.route("/workheights.html")
def workheights():
    image_folder = os.path.join(app.static_folder, 'assets/고소작업행동절차workheights')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('workheights.html', images=image_files)

@app.route("/manhowork.html")
def manhowork():
    image_folder = os.path.join(app.static_folder, 'assets/맨홀작업행동절차manhowork')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('manhowork.html', images=image_files)

@app.route("/signalman.html")
def signalman():
    image_folder = os.path.join(app.static_folder, 'assets/신호수,방호차량기준signalman')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('signalman.html', images=image_files)

@app.route("/roadcontrol.html")
def roadcontrol():
    image_folder = os.path.join(app.static_folder, 'assets/구간별도로통제절차roadcontrol')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('roadcontrol.html', images=image_files)

@app.route("/ytbucketvehiclework.html")
def ytbucketvehiclework():
    image_folder = os.path.join(app.static_folder, 'assets/ytbucketvehiclework')
    # 이미지 파일 목록을 가져오고 확장자가 jpg 또는 png인 파일만 선택
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    # 파일명을 정렬 (숫자가 포함된 경우 순서대로 표시)
    image_files.sort()
    return render_template('ytbucketvehiclework.html', images=image_files)

if __name__ == "__main__":
    app.run(debug=True)
