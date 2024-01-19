import gradio as gr
import pdb

def test():
    pdb.set_trace()
    # if_label.update({"value":False})
    # for key in dir(if_label):
    #     print(key,eval("if_label.%s" % key))

    # yield if_label_value

with gr.Blocks(title="RVC WebUI") as app:
    gr.Markdown(
        value=
            "本软件以MIT协议开源, 作者不对软件具备任何控制力, 使用软件者、传播软件导出的声音者自负全责. <br>如不认可该条款, 则不能使用或引用软件包内任何代码和文件. 详见根目录<b>LICENSE</b>."
    )
    with gr.Tabs():
        with gr.TabItem("模型推理"):
            with gr.Row():
                # if_label = gr.Checkbox(label="是否开启打标WebUI",show_label=True,value=True,interactive=True)
                # asr_inp_dir = gr.Textbox(
                #     label="批量ASR(中文only)输入文件夹路径",
                #     value="D:\\RVC1006\\GPT-SoVITS\\raw",
                #     interactive=True,
                # )
                button = gr.Button("开启离线批量ASR", variant="primary",interactive=False)
                button.click(test)
    # if_label.change(test,[if_label],[if_label])
    # if_label.change(test,[],[])
app.launch(
    server_name="0.0.0.0",
    inbrowser=True,
    server_port=9875,
    quiet=True,
)