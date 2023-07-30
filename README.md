## my env
### system env:
1. win 10 64 bit
2. windows git shell command line

### software env:
1. python                    3.8 64 bit
2. paddleocr                 2.6.1.3
3. paddlepaddle              2.5.0
4. pyinstaller               5.13.0
5. pyinstaller-hooks-contrib 2023.5

### how to reproduce issue mentioned by PR https://github.com/PaddlePaddle/PaddleOCR/pull/10421
```
$ python -m pip install -r requirements.txt
$ python to_exe.py
$ cd dist
$ ./main.exe
```

```
Traceback (most recent call last):
  File "main.py", line 4, in <module>
  File "PyInstaller\loader\pyimod02_importers.py", line 385, in exec_module
  File "paddleocr\__init__.py", line 14, in <module>
  File "PyInstaller\loader\pyimod02_importers.py", line 385, in exec_module
  File "paddleocr\paddleocr.py", line 33, in <module>
  File "importlib\__init__.py", line 127, in import_module
ModuleNotFoundError: No module named 'tools'
[36268] Failed to execute script 'main' due to unhandled exception!
```

### how to fix it
1. use modified paddleocr module code ( as the way by https://github.com/PaddlePaddle/PaddleOCR/pull/10421 ), replace into python root path's Lib\site-packages\paddleocr\  directory.
```
cd /path/to/python/Lib/site-packages/
rm -rf paddleocr
git clone https://github.com/kerneltravel/PaddleOCR_Lib_site-packages_paddleocr_fixed  paddleocr
```

2. cd to_exe.py's directory 
3. 
```
rm -rf  dist/ 
```
4. 
```
python to_exe.py
```
5. 
```
cd dist/
```
6. 
```
./main.exe
```
[works well, will output as bellow]
```
[2023/07/19 22:13:39] ppocr DEBUG: Namespace(alpha=1.0, benchmark=False, beta=1.0, cls_batch_num=6, cls_image_shape='3, 48, 192', cls_model_dir='……/.paddleocr/whl\\cls\\ch_ppocr_mobile_v2.0_cls_infer', cls_thresh=0.9, cpu_threads=10, crop_res_save_dir='./output', det=True, det_algorithm='DB', det_box_type='quad', det_db_box_thresh=0.6, det_db_score_mode='fast', det_db_thresh=0.3, det_db_unclip_ratio=1.5, det_east_cover_thresh=0.1, det_east_nms_thresh=0.2, det_east_score_thresh=0.8, det_limit_side_len=960, det_limit_type='max', det_model_dir='……/.paddleocr/whl\\det\\ch\\ch_PP-OCRv3_det_infer', det_pse_box_thresh=0.85, det_pse_min_area=16, det_pse_scale=1, det_pse_thresh=0, det_sast_nms_thresh=0.2, det_sast_score_thresh=0.5, draw_img_save_dir='./inference_results', drop_score=0.5, e2e_algorithm='PGNet', e2e_char_dict_path='./ppocr/utils/ic15_dict.txt', e2e_limit_side_len=768, e2e_limit_type='max', e2e_model_dir=None, e2e_pgnet_mode='fast', e2e_pgnet_score_thresh=0.5, e2e_pgnet_valid_set='totaltext', enable_mkldnn=False, fourier_degree=5, gpu_mem=500, help='==SUPPRESS==', image_dir=None, image_orientation=False, ir_optim=True, kie_algorithm='LayoutXLM', label_list=['0', '180'], lang='ch', layout=True, layout_dict_path=None, layout_model_dir=None, layout_nms_threshold=0.5, layout_score_threshold=0.5, max_batch_size=10, max_text_length=25, merge_no_span_structure=True, min_subgraph_size=15, mode='structure', ocr=True, ocr_order_method=None, ocr_version='PP-OCRv3', output='./output', page_num=0, precision='fp32', process_id=0, re_model_dir=None, rec=True, rec_algorithm='SVTR_LCNet', rec_batch_num=6, rec_char_dict_path='……\\paddleocr\\ppocr\\utils\\ppocr_keys_v1.txt', rec_image_inverse=True, rec_image_shape='3, 48, 320', rec_model_dir='……/.paddleocr/whl\\rec\\ch\\ch_PP-OCRv3_rec_infer', recovery=False, save_crop_res=False, save_log_path='./log_output/', scales=[8, 16, 32], ser_dict_path='../train_data/XFUND/class_list_xfun.txt', ser_model_dir=None, show_log=True, sr_batch_num=1, sr_image_shape='3, 32, 128', sr_model_dir=None, structure_version='PP-StructureV2', table=True, table_algorithm='TableAttn', table_char_dict_path=None, table_max_len=488, table_model_dir=None, total_process_num=1, type='ocr', use_angle_cls=True, use_dilation=False, use_gpu=False, use_mp=False, use_npu=False, use_onnx=False, use_pdf2docx_api=False, use_pdserving=False, use_space_char=True, use_tensorrt=False, use_visual_backbone=True, use_xpu=False, vis_font_path='./doc/fonts/simfang.ttf', warmup=False)
[2023/07/19 22:13:40] ppocr DEBUG: dt_boxes num : 16, elapse : 0.24251461029052734
[2023/07/19 22:13:40] ppocr DEBUG: cls num  : 16, elapse : 0.1781299114227295
[2023/07/19 22:13:43] ppocr DEBUG: rec_res num  : 16, elapse : 3.1375880241394043
[[[28.0, 37.0], [302.0, 39.0], [302.0, 72.0], [27.0, 70.0]], ('纯臻营养护发素', 0.9658750295639038)]
[[[26.0, 81.0], [172.0, 83.0], [172.0, 104.0], [25.0, 101.0]], ('产品信息/参数', 0.9113165736198425)]
[[[28.0, 115.0], [330.0, 115.0], [330.0, 132.0], [28.0, 132.0]], ('（45元/每公斤，100公斤起订）', 0.8843317031860352)]
[[[27.0, 145.0], [282.0, 145.0], [282.0, 164.0], [27.0, 164.0]], ('每瓶22元，1000瓶起订）', 0.9211593270301819)]
[[[26.0, 179.0], [299.0, 179.0], [299.0, 195.0], [26.0, 195.0]], ('【品牌】：代加工方式/OEMODM', 0.9661461114883423)]
[[[26.0, 210.0], [233.0, 210.0], [233.0, 227.0], [26.0, 227.0]], ('【品名】：纯臻营养护发素', 0.8831911087036133)]
[[[26.0, 241.0], [241.0, 241.0], [241.0, 258.0], [26.0, 258.0]], ('【产品编号】：YM-X-3011', 0.8718017339706421)]
[[[413.0, 236.0], [430.0, 236.0], [430.0, 303.0], [413.0, 303.0]], ('ODMOEM', 0.9539504647254944)]
[[[23.0, 271.0], [180.0, 269.0], [180.0, 289.0], [24.0, 290.0]], ('【净含量】：220ml', 0.9348616003990173)]
[[[26.0, 304.0], [252.0, 304.0], [252.0, 320.0], [26.0, 320.0]], ('适用人群）：适合所有肤质', 0.8866138458251953)]
[[[26.0, 335.0], [343.0, 335.0], [343.0, 352.0], [26.0, 352.0]], ('【主要成分】：鲸蜡硬脂醇、燕麦β-葡聚', 0.9245778322219849)]
[[[27.0, 366.0], [281.0, 366.0], [281.0, 383.0], [27.0, 383.0]], ('糖、椰油酰胺丙基甜菜碱、泛醒', 0.9368152618408203)]
[[[369.0, 370.0], [477.0, 370.0], [477.0, 387.0], [369.0, 387.0]], ('（成品包材）', 0.8927490711212158)]
[[[26.0, 397.0], [361.0, 397.0], [361.0, 414.0], [26.0, 414.0]], ('【主要功能】：可紧致头发磷层，从而达到', 0.8677802085876465)]
[[[28.0, 429.0], [372.0, 429.0], [372.0, 445.0], [28.0, 445.0]], ('即时持久改善头发光泽的效果，给于燥的头', 0.8803297281265259)]
[[[27.0, 459.0], [136.0, 459.0], [136.0, 479.0], [27.0, 479.0]], ('发足够的滋养', 0.9091537594795227)]
```

so the above TWO steps , illustrate how to reproduce and how to fix .
