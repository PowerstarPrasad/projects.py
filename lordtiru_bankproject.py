<!DOCTYPE html>
<!-- saved from url=(0076)https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py -->
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system" data-turbo-loaded=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style>.ͼ1.cm-focused {outline: 1px dotted #212121;}
.ͼ1 {position: relative !important; box-sizing: border-box; display: flex !important; flex-direction: column;}
.ͼ1 .cm-scroller {display: flex !important; align-items: flex-start !important; font-family: monospace; line-height: 1.4; height: 100%; overflow-x: auto; position: relative; z-index: 0;}
.ͼ1 .cm-content[contenteditable=true] {-webkit-user-modify: read-write-plaintext-only;}
.ͼ1 .cm-content {margin: 0; flex-grow: 2; flex-shrink: 0; display: block; white-space: pre; word-wrap: normal; box-sizing: border-box; padding: 4px 0; outline: none;}
.ͼ1 .cm-lineWrapping {white-space: pre-wrap; white-space: break-spaces; word-break: break-word; overflow-wrap: anywhere; flex-shrink: 1;}
.ͼ2 .cm-content {caret-color: black;}
.ͼ3 .cm-content {caret-color: white;}
.ͼ1 .cm-line {display: block; padding: 0 2px 0 6px;}
.ͼ1 .cm-layer > * {position: absolute;}
.ͼ1 .cm-layer {position: absolute; left: 0; top: 0; contain: size style;}
.ͼ2 .cm-selectionBackground {background: #d9d9d9;}
.ͼ3 .cm-selectionBackground {background: #222;}
.ͼ2.cm-focused .cm-selectionBackground {background: #d7d4f0;}
.ͼ3.cm-focused .cm-selectionBackground {background: #233;}
.ͼ1 .cm-cursorLayer {pointer-events: none;}
.ͼ1.cm-focused .cm-cursorLayer {animation: steps(1) cm-blink 1.2s infinite;}
@keyframes cm-blink {50% {opacity: 0;}}
@keyframes cm-blink2 {50% {opacity: 0;}}
.ͼ1 .cm-cursor, .ͼ1 .cm-dropCursor {border-left: 1.2px solid black; margin-left: -0.6px; pointer-events: none;}
.ͼ1 .cm-cursor {display: none;}
.ͼ3 .cm-cursor {border-left-color: #444;}
.ͼ1 .cm-dropCursor {position: absolute;}
.ͼ1.cm-focused .cm-cursor {display: block;}
.ͼ2 .cm-activeLine {background-color: #cceeff44;}
.ͼ3 .cm-activeLine {background-color: #99eeff33;}
.ͼ2 .cm-specialChar {color: red;}
.ͼ3 .cm-specialChar {color: #f78;}
.ͼ1 .cm-gutters {flex-shrink: 0; display: flex; height: 100%; box-sizing: border-box; left: 0; z-index: 200;}
.ͼ2 .cm-gutters {background-color: #f5f5f5; color: #6c6c6c; border-right: 1px solid #ddd;}
.ͼ3 .cm-gutters {background-color: #333338; color: #ccc;}
.ͼ1 .cm-gutter {display: flex !important; flex-direction: column; flex-shrink: 0; box-sizing: border-box; min-height: 100%; overflow: hidden;}
.ͼ1 .cm-gutterElement {box-sizing: border-box;}
.ͼ1 .cm-lineNumbers .cm-gutterElement {padding: 0 3px 0 5px; min-width: 20px; text-align: right; white-space: nowrap;}
.ͼ2 .cm-activeLineGutter {background-color: #e2f2ff;}
.ͼ3 .cm-activeLineGutter {background-color: #222227;}
.ͼ1 .cm-panels {box-sizing: border-box; position: sticky; left: 0; right: 0;}
.ͼ2 .cm-panels {background-color: #f5f5f5; color: black;}
.ͼ2 .cm-panels-top {border-bottom: 1px solid #ddd;}
.ͼ2 .cm-panels-bottom {border-top: 1px solid #ddd;}
.ͼ3 .cm-panels {background-color: #333338; color: white;}
.ͼ1 .cm-tab {display: inline-block; overflow: hidden; vertical-align: bottom;}
.ͼ1 .cm-widgetBuffer {vertical-align: text-top; height: 1em; width: 0; display: inline;}
.ͼ1 .cm-placeholder {color: #888; display: inline-block; vertical-align: top;}
.ͼ1 .cm-highlightSpace:before {content: attr(data-display); position: absolute; pointer-events: none; color: #888;}
.ͼ1 .cm-highlightTab {background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="200" height="20"><path stroke="%23888" stroke-width="1" fill="none" d="M1 10H196L190 5M190 15L196 10M197 4L197 16"/></svg>'); background-size: auto 100%; background-position: right 90%; background-repeat: no-repeat;}
.ͼ1 .cm-trailingSpace {background-color: #ff332255;}
.ͼ1 .cm-button {vertical-align: middle; color: inherit; font-size: 70%; padding: .2em 1em; border-radius: 1px;}
.ͼ2 .cm-button:active {background-image: linear-gradient(#b4b4b4, #d0d3d6);}
.ͼ2 .cm-button {background-image: linear-gradient(#eff1f5, #d9d9df); border: 1px solid #888;}
.ͼ3 .cm-button:active {background-image: linear-gradient(#111, #333);}
.ͼ3 .cm-button {background-image: linear-gradient(#393939, #111); border: 1px solid #888;}
.ͼ1 .cm-textfield {vertical-align: middle; color: inherit; font-size: 70%; border: 1px solid silver; padding: .2em .5em;}
.ͼ2 .cm-textfield {background-color: white;}
.ͼ3 .cm-textfield {border: 1px solid #555; background-color: inherit;}
.ͼ1 .cm-panel.cm-search [name=close] {position: absolute; top: 0; right: 4px; background-color: inherit; border: none; font: inherit; padding: 0; margin: 0;}
.ͼ1 .cm-panel.cm-search input, .ͼ1 .cm-panel.cm-search button, .ͼ1 .cm-panel.cm-search label {margin: .2em .6em .2em 0;}
.ͼ1 .cm-panel.cm-search input[type=checkbox] {margin-right: .2em;}
.ͼ1 .cm-panel.cm-search label {font-size: 80%; white-space: pre;}
.ͼ1 .cm-panel.cm-search {padding: 2px 6px 4px; position: relative;}
.ͼ2 .cm-searchMatch {background-color: #ffff0054;}
.ͼ3 .cm-searchMatch {background-color: #00ffff8a;}
.ͼ2 .cm-searchMatch-selected {background-color: #ff6a0054;}
.ͼ3 .cm-searchMatch-selected {background-color: #ff00ff8a;}
.ͼ1.cm-focused .cm-matchingBracket {background-color: #328c8252;}
.ͼ1.cm-focused .cm-nonmatchingBracket {background-color: #bb555544;}
.ͼ6 {color: var(--color-codemirror-syntax-keyword);}
.ͼ7 {color: var(--color-codemirror-syntax-comment);}
.ͼ8 {color: var(--color-codemirror-matchingbracket-text);}
.ͼ9 {color: var(--color-codemirror-syntax-string);}
.ͼa {color: var(--color-codemirror-syntax-constant);}
.ͼb {color: var(--color-codemirror-syntax-constant);}
.ͼc {color: var(--color-codemirror-syntax-entity);}
.ͼd {color: var(--color-codemirror-syntax-variable);}
.ͼe {color: inherit;}
.ͼf {font-weight: bold; color: inherit !important;}
.ͼg {text-decoration: underline;}
.ͼh {font-style: italic;}
.ͼi {font-weight: bold;}
.ͼj {text-decoration: line-through;}
.ͼ5 {background: var(--color-codemirror-bg); color: var(--color-codemirror-text);}
.ͼ5 .cm-gutters {background: var(--color-codemirror-gutters-bg); border-right-width: 0;}
.ͼ5 .cm-lineNumbers .cm-gutterElement {color: var(--color-codemirror-linenumber-text); padding: 0 16px 0 16px;}
.ͼ5 .cm-content {caret-color: var(--color-codemirror-cursor); font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace; font-size: 12px; background: var(--color-codemirror-lines-bg); line-height: 20px; padding-top: 8px;}
.ͼ5.cm-focused .cm-selectionBackground, .ͼ5 .cm-selectionBackground, .ͼ5 .cm-content ::selection {background-color: var(--color-codemirror-selection-bg, #d7d4f0);}
.ͼ5.cm-focused {outline: none;}
.ͼ5 .cm-content ::-moz-selection {background-color: var(--color-codemirror-selection-bg, #d7d4f0);}
.ͼ5 .cm-activeLine {background-color: var(--color-codemirror-activeline-bg);}
.ͼ5 .cm-line {padding-left: 16px;}
.ͼ5 .cm-help-panel {background: var(--color-canvas-subtle); padding: 7px 10px; margin: 0; font-size: 13px; line-height: 16px; color: var(--color-fg-muted);}
.ͼ5 .cm-panels-bottom {border-top: var(--borderWidth-thin, 1px) solid var(--color-border-default); background: none;}
.ͼ5 .cm-panel.cm-search {background: var(--color-canvas-subtle); padding: 8px; font-size: 16px;}
.ͼ5 .cm-panel.cm-search > button {border-radius: 6px; padding: 4px 8px; background: var(--color-codemirror-bg); color: var(--color-btn-text); border: 1px solid var(--color-btn-border); text-transform: capitalize;}
.ͼ5 .cm-panel.cm-search > label {color: var(--color-fg-default); text-transform: capitalize; font-size: 12px;}
.ͼ5 .cm-panel.cm-search > input {border-radius: 6px; padding: 4px 8px; background: var(--color-canvas-default); color: var(--color-fg-default); border: 1px solid var(--color-border-default); font-size: 12px;}
.ͼ5 .cm-panel.cm-search > button[name="close"] {padding: 4px;}
.ͼ5 .cm-panels-top {border-bottom: var(--borderWidth-thin, 1px) solid var(--color-border-default); background: none;}
.ͼ5 .cm-panel.cm-search input, .ͼ5 .cm-panel.cm-search button, .ͼ5 .cm-panel.cm-search label {margin-right: 8px; margin-bottom: 4px; margin-top: 4px; margin-left: 0;}
.ͼk {height: 70vh; min-height: ; width: 100%;}
.ͼ4 {height: 70vh; min-height: ; width: 100%;}
</style><style type="text/css">.turbo-progress-bar {
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  height: 3px;
  background: #0076ff;
  z-index: 2147483647;
  transition:
    width 300ms ease-out,
    opacity 150ms 150ms ease-in;
  transform: translate3d(0, 0, 0);
}
</style>
    
  
  
  
  
  
  

  

  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./lordtiru_bankproject_files/light-946902aac6a1.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./lordtiru_bankproject_files/dark-030e28cb8394.css"><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-53fac7eeaef0.css"><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-e7297f24f20e.css"><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-2c82e49ee788.css"><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-b3c5f4428be3.css"><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-b249b3c5ff73.css"><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-413c5e259397.css"><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-7690b6bac103.css">
  
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./lordtiru_bankproject_files/primer-primitives-fb1d51d1ef66.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./lordtiru_bankproject_files/primer-7e8db5e0affc.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./lordtiru_bankproject_files/global-a55bf4a27d6d.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./lordtiru_bankproject_files/github-1c76916a54fc.css">
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./lordtiru_bankproject_files/code-554c92b43987.css">

    


  <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/wp-runtime-b326bc71b00f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_stacktrace-parser_dist_stack-trace-parser_esm_js-node_modules_github_bro-a4c183-ae93d3fba59c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/ui_packages_soft-nav_soft-nav_ts-899d6d5b0d82.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/environment-07edc14d05eb.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_github_selector-observer_dist_index_esm_js-2646a2c533e3.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_github_relative-time-element_dist_index_js-99e288659d4f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_fzy_js_index_js-node_modules_github_markdown-toolbar-element_dist_index_js-e3de700a4c9d.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_auto-complete-element-5b3870-ff38694180c6.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_github_text-ex-3415a8-7ecc10fb88d0.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-8873b7-5771678648e0.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_primer_view-components_app_components_primer_primer_js-node_modules_gith-3af896-ffd63f7f2a27.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/github-elements-433bc7a3c486.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/element-registry-5fca7780689f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_lit-html_lit-html_js-9d9fe1859ce5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_morphdom_dist_morphdom-esm_js-b1fdd7158cf0.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_alive-client_dist-bf5aa2-424aa982deef.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-ba0e4d5b3207.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_color-convert_index_js-node_modules_github_jtml_lib_index_js-40bf234a19dc.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_scroll-anchoring_dist_scro-52dc4b-e1e33bfc0b7e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_github_paste-markdown_dist_index_esm_js-node_modules_github_quote-select-743f1d-1b20d530fbf0.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/app_assets_modules_github_updatable-content_ts-88070db28a55.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/app_assets_modules_github_behaviors_keyboard-shortcuts-helper_ts-app_assets_modules_github_be-f5afdb-3a77a772cd4d.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/app_assets_modules_github_sticky-scroll-into-view_ts-050ad6637d58.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-2e2258-7effad8d88d4.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-f22ac6b94445.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/app_assets_modules_github_blob-anchor_ts-app_assets_modules_github_filter-sort_ts-app_assets_-e5f169-c54621d9e188.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/behaviors-a2fb1d158d27.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-623425af41e1.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/notifications-global-0104a8043aa4.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_optimizely_optimizely-sdk_dist_optimizely_browser_es_min_js-node_modules-089adc-2328ba323205.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/optimizely-c6fa9687eddf.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_virtualized-list_es_index_js-node_modules_github_template-parts_lib_index_js-677582870bfd.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-911b971-b9c79ae563e3.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/app_assets_modules_github_ref-selector_ts-0e2b12902d39.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/codespaces-a23712a0ec52.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_github_remote-form_-e3de2b-779fd9166293.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_github_filter--b2311f-15fe0f17a114.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/repositories-71781dca4d5e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_index_js-0cc53ae22129.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/topic-suggestions-63dafebaad28.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/code-menu-7dfb8cccdca1.js.download"></script>
  

  



  

    
  


  


    


  
  

  
  

    
  
  
  
  



  

  




  

    

  

    
    
      
      
    
    
    
      
      
      

      
      


        


      

        

    


  <meta http-equiv="x-pjax-version" content="3e9efc3dd8b92a97839c775ac6c6507f35ab135ce73ba75d0133424bcee1d0ff" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="0db263f9a873141d8256f783c35f244c06d490aacc3b680f99794dd8fd59fb59" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="7653487bcb00746ee53965d18a1cfa9141ce2a2b7fd4e326d429793c8a55ad42" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="ebe6af43c3d268c081f399069b557c35cf24ed8b4d5009dd8d0060f8f3d786ae" data-turbo-track="reload">

  

    
  

  



    
  


  

  

  

  
  
  





  

  <script type="application/javascript" src="./lordtiru_bankproject_files/react-lib-210c4b5934c3.js.download"></script><script type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_primer_octicons-react_dist_index_esm_js-node_modules_primer_react_lib-es-ca6dae-79715380a9e2.js.download"></script><script type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_primer_react_lib-esm_Button_Button_js-node_modules_primer_react_lib-esm_-1523be-44ddafc1a22a.js.download"></script><script type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_primer_react_lib-esm_ActionList_index_js-node_modules_primer_react_lib-e-0492ff-af7c32b3c84f.js.download"></script><script type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_primer_react_lib-esm_TextInput_TextInput_js-4e2cb563b537.js.download"></script><script type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_dompurify_dist_purify_js-64d590970fa6.js.download"></script><script type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_primer_react_lib-esm_deprecated_ActionList_index_js-node_modules_primer_-fed12b-aab66293925c.js.download"></script><script type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_primer_react_lib-esm_FormControl_FormControl_js-785e3d3ff3f3.js.download"></script><script type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_primer_react_lib-esm_Dialog_js-node_modules_primer_react_lib-esm_Flash_F-54f402-6ec15f63be32.js.download"></script><script type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_primer_react_lib-esm_AnchoredOverlay_AnchoredOverlay_js-node_modules_pri-103317-effd4dd38074.js.download"></script><script type="application/javascript" src="./lordtiru_bankproject_files/ui_packages_react-core_deferred-registry_ts-ui_packages_react-core_AppContextProvider_tsx-ui_-36d03f-4df952ab6fe3.js.download"></script><script type="application/javascript" src="./lordtiru_bankproject_files/ui_packages_ref-selector_RefSelector_tsx-ui_packages_safe-html_SafeHTML_tsx-77654c1f984d.js.download"></script><script type="application/javascript" src="./lordtiru_bankproject_files/create-branch-button-a9ff79beb866.js.download"></script><style data-styled="active" data-styled-version="5.3.6"></style><script type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_ActionMenu_js-node_modules_primer_react_lib-esm_Sty-aa3149-e33bed59a504.js"></script><script type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Heading_Heading_js-node_modules_primer_react_lib-es-20c766-2f73d206e824.js"></script><script type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_focus-zone_js-e11d55a242ff.js"></script><script type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Dialog_ConfirmationDialog_js-87d8bd9c967a.js"></script><script type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_TreeView_TreeView_js-7165830dc4a6.js"></script><script type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_blackbird-parser_dist_blackbird_js-fcd9d30e9b7e.js"></script><script type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Avatar_Avatar_js-node_modules_primer_react_lib-esm_-b3e5c3-84ac1a3f199c.js"></script><script type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_anchored-position_js-node_modules_primer_react-5771ad-8bb3bbcef740.js"></script><script type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_UnderlineNav2_index_js-0f3ba9d900a1.js"></script><script type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_scroll-into-view_js-node_modules_primer_react_-282458-f52259b5041a.js"></script><script type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_react-core_Entry_tsx-d7bb6c9e07f2.js"></script><script type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_blackbird-monolith_hooks_use-navigate-to-query_ts-app_assets_modules_black-8527d4-2c5398859eee.js"></script><script type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_react-code-view_pages_CodeView_tsx-d54e08d986b9.js"></script><script type="application/javascript" src="https://github.githubassets.com/assets/react-code-view-9642743d6fa6.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_clipboard-copy-element_dist_index_esm_js-node_modules_scroll-anch-c93c97-d63d35dd5d0b.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_diffs_blob-lines_ts-app_assets_modules_github_diffs_linkable-line-n-ed3f24-df2ee88d2412.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/diffs-8034c45b6f12.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/react-lib-210c4b5934c3.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_primer_octicons-react_dist_index_esm_js-node_modules_primer_react_lib-es-ca6dae-79715380a9e2.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_primer_react_lib-esm_Button_Button_js-node_modules_primer_react_lib-esm_-1523be-44ddafc1a22a.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_primer_react_lib-esm_ActionList_index_js-node_modules_primer_react_lib-e-0492ff-af7c32b3c84f.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_primer_react_lib-esm_TextInput_TextInput_js-4e2cb563b537.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_dompurify_dist_purify_js-64d590970fa6.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_primer_react_lib-esm_deprecated_ActionList_index_js-node_modules_primer_-fed12b-aab66293925c.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_primer_react_lib-esm_FormControl_FormControl_js-785e3d3ff3f3.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_ActionMenu_js-node_modules_primer_react_lib-esm_Sty-aa3149-e33bed59a504.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Heading_Heading_js-node_modules_primer_react_lib-es-20c766-2f73d206e824.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_focus-zone_js-e11d55a242ff.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Dialog_ConfirmationDialog_js-87d8bd9c967a.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_TreeView_TreeView_js-7165830dc4a6.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_primer_react_lib-esm_Dialog_js-node_modules_primer_react_lib-esm_Flash_F-54f402-6ec15f63be32.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_blackbird-parser_dist_blackbird_js-fcd9d30e9b7e.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Avatar_Avatar_js-node_modules_primer_react_lib-esm_-b3e5c3-84ac1a3f199c.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_anchored-position_js-node_modules_primer_react-5771ad-8bb3bbcef740.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_UnderlineNav2_index_js-0f3ba9d900a1.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_scroll-into-view_js-node_modules_primer_react_-282458-f52259b5041a.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/ui_packages_react-core_deferred-registry_ts-ui_packages_react-core_AppContextProvider_tsx-ui_-36d03f-4df952ab6fe3.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_react-core_Entry_tsx-d7bb6c9e07f2.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/ui_packages_ref-selector_RefSelector_tsx-ui_packages_safe-html_SafeHTML_tsx-77654c1f984d.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_blackbird-monolith_hooks_use-navigate-to-query_ts-app_assets_modules_black-8527d4-2c5398859eee.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_react-code-view_pages_CodeView_tsx-d54e08d986b9.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/react-code-view-9642743d6fa6.js"></script><script type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_primer_behaviors_dist_es-de2bcd-5e345baf81c7.js"></script><script type="application/javascript" src="https://github.githubassets.com/assets/issues-5418e36da5d0.js"></script><script type="application/javascript" src="https://github.githubassets.com/assets/structured-issues-613adf1b1211.js"></script><link rel="dns-prefetch" href="https://github.githubassets.com/"><link rel="dns-prefetch" href="https://avatars.githubusercontent.com/"><link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/"><link rel="dns-prefetch" href="https://user-images.githubusercontent.com/"><link rel="preconnect" href="https://github.githubassets.com/" crossorigin=""><link rel="preconnect" href="https://avatars.githubusercontent.com/"><title>Editing projects_5/railway project.py at main · PowerstarPrasad/projects_5 · GitHub</title><meta name="route-pattern" content="/:user_id/:repository/blob/*name(/*path)"><meta name="current-catalog-service-hash" content="82c569b93da5c18ed649ebd4c2c79437db4611a6a1373e805a3cb001c64130b7"><meta name="request-id" content="FEFE:7DD3:3A776E:3E232A:6491BA6E" data-turbo-transient="true"><meta name="html-safe-nonce" content="6893b313c66cfa511b9c705c753c3759be87aa3ba5c01350bc407fccdcb923b8" data-turbo-transient="true"><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9Qb3dlcnN0YXJQcmFzYWQvcHJvamVjdHNfNS9ibG9iL21haW4vcmFpbHdheSUyMHByb2plY3QucHkiLCJyZXF1ZXN0X2lkIjoiRkVGRTo3REQzOjNBNzc2RTozRTIzMkE6NjQ5MUJBNkUiLCJ2aXNpdG9yX2lkIjoiNjE5NjAyNDQ2MzQ4NTYxMzc0IiwicmVnaW9uX2VkZ2UiOiJjZW50cmFsaW5kaWEiLCJyZWdpb25fcmVuZGVyIjoiaWFkIn0=" data-turbo-transient="true"><meta name="visitor-hmac" content="d65915688db5d9f3be442d7ae3e28d5af90925319d6cc3f5277907b6b35f59ea" data-turbo-transient="true"><meta name="hovercard-subject-tag" content="repository:656240539" data-turbo-transient=""><meta name="github-keyboard-shortcuts" content="repository,source-code,file-tree" data-turbo-transient="true"><meta name="selected-link" value="repo_source" data-turbo-transient=""><link rel="assets" href="https://github.githubassets.com/"><meta name="google-site-verification" content="c1kuD-K2HIVF635lypcsWPoD4kilo5-jA_wBFyT4uMY"><meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU"><meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA"><meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc"><meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I"><meta name="octolytics-url" content="https://collector.github.com/github/collect"><meta name="octolytics-actor-id" content="137187658"><meta name="octolytics-actor-login" content="PowerstarPrasad"><meta name="octolytics-actor-hash" content="f157f0f246602df53273df30d7550bf4d5eb062ebf141af0a0723fa19a5fb6be"><meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-turbo-transient="true"><meta name="user-login" content="PowerstarPrasad"><link rel="sudo-modal" href="https://github.com/sessions/sudo_modal"><meta name="enabled-features" content="TURBO_EXPERIMENT_RISKY,IMAGE_METRIC_TRACKING,GEOJSON_AZURE_MAPS"><meta name="turbo-cache-control" content="no-preview" data-turbo-transient=""><meta name="turbo-cache-control" content="no-cache" data-turbo-transient=""><meta data-hydrostats="publish"><meta name="go-import" content="github.com/PowerstarPrasad/projects_5 git https://github.com/PowerstarPrasad/projects_5.git"><meta name="octolytics-dimension-user_id" content="137187658"><meta name="octolytics-dimension-user_login" content="PowerstarPrasad"><meta name="octolytics-dimension-repository_id" content="656240539"><meta name="octolytics-dimension-repository_nwo" content="PowerstarPrasad/projects_5"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="true"><meta name="octolytics-dimension-repository_parent_id" content="639066377"><meta name="octolytics-dimension-repository_parent_nwo" content="venkatesh-gorrela/projects_5"><meta name="octolytics-dimension-repository_network_root_id" content="639066377"><meta name="octolytics-dimension-repository_network_root_nwo" content="venkatesh-gorrela/projects_5"><meta name="turbo-body-classes" content="logged-in env-production page-responsive"><meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats"><meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors"><meta name="browser-optimizely-client-errors-url" content="https://api.github.com/_private/browser/optimizely_client/errors"><link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000"><link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon-dark.png"><link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon-dark.svg"><meta name="theme-color" content="#1e2327"><meta name="color-scheme" content="light dark"><link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials"></head>

  <div class="turbo-progress-bar" style="width: 10%; opacity: 1;"></div><body class="logged-in env-production page-responsive intent-mouse" style="word-wrap: break-word;">
    <div data-turbo-body="" class="logged-in env-production page-responsive" style="word-wrap: break-word;">
      


    <div class="position-relative js-header-wrapper ">
      <a href="https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py#start-of-content" class="p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>
      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      


        <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_allex_crc32_lib_crc32_esm_js-node_modules_github_mini-throttle_dist_deco-26fa0f-02e7ed68dae1.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/vendors-node_modules_github_clipboard-copy-element_dist_index_esm_js-node_modules_delegated-e-b37f7d-a9177ba414f2.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/app_assets_modules_github_command-palette_items_help-item_ts-app_assets_modules_github_comman-48ad9d-f882e479ad2f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./lordtiru_bankproject_files/command-palette-13bd844fa1c6.js.download"></script>

            <header class="AppHeader">
    <div class="AppHeader-globalBar pb-2 js-global-bar">
      <div class="AppHeader-globalBar-start">
          <deferred-side-panel data-url="/_side-panels/global" data-catalyst="">
  <include-fragment data-target="deferred-side-panel.fragment"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
      
  <button aria-label="Open global navigation menu" data-action="click:deferred-side-panel#loadPanel click:deferred-side-panel#panelOpened" data-show-dialog-id="dialog-a942e936-ec65-4639-a90c-8fb6d4885b58" id="dialog-show-dialog-a942e936-ec65-4639-a90c-8fb6d4885b58" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-bg-transparent p-0 color-fg-muted" fdprocessedid="sxgoal">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-three-bars Button-visual">
    <path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75Zm0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75ZM1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Z"></path>
</svg>
</button>  

<div class="Overlay--hidden Overlay-backdrop--side Overlay-backdrop--placement-left" data-modal-dialog-overlay="">
  <modal-dialog data-target="deferred-side-panel.panel" role="dialog" id="dialog-a942e936-ec65-4639-a90c-8fb6d4885b58" aria-modal="true" aria-disabled="true" aria-describedby="dialog-a942e936-ec65-4639-a90c-8fb6d4885b58-title dialog-a942e936-ec65-4639-a90c-8fb6d4885b58-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade SidePanel" style="max-height: 714px;">
    <div styles="flex-direction: row;" data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="dialog-a942e936-ec65-4639-a90c-8fb6d4885b58-title">
        Global navigation
      </h1>
            <div data-view-component="true" class="d-flex">
      <div data-view-component="true" class="AppHeader-logo position-relative">
        <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
</div></div>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="dialog-a942e936-ec65-4639-a90c-8fb6d4885b58" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body d-flex flex-column height-full px-2">      <nav aria-label="Site navigation" data-view-component="true" class="ActionList">
  
  <nav-list data-catalyst="">
    <ul data-view-component="true" class="ActionListWrap">
        
          
<li item_id="general" data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-hotkey="g d" hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py&quot;,&quot;target&quot;:&quot;HOME&quot;,&quot;originating_url&quot;:&quot;https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py&quot;,&quot;user_id&quot;:137187658}}" hydro-click-hmac="85f4a3f3661c9918b924a490c9567f023a30b74612b8829a4ebecd7bd50039ff" id="item-bdbaad37-77e1-4c10-8081-a6c68d58d4e2" href="https://github.com/dashboard" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-home">
    <path d="M6.906.664a1.749 1.749 0 0 1 2.187 0l5.25 4.2c.415.332.657.835.657 1.367v7.019A1.75 1.75 0 0 1 13.25 15h-3.5a.75.75 0 0 1-.75-.75V9H7v5.25a.75.75 0 0 1-.75.75h-3.5A1.75 1.75 0 0 1 1 13.25V6.23c0-.531.242-1.034.657-1.366l5.25-4.2Zm1.25 1.171a.25.25 0 0 0-.312 0l-5.25 4.2a.25.25 0 0 0-.094.196v7.019c0 .138.112.25.25.25H5.5V8.25a.75.75 0 0 1 .75-.75h3.5a.75.75 0 0 1 .75.75v5.25h2.75a.25.25 0 0 0 .25-.25V6.23a.25.25 0 0 0-.094-.195Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Home
</span></a>
  
  
</li>

        
          
<li item_id="personal_info" data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-hotkey="g i" hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py&quot;,&quot;target&quot;:&quot;ISSUES&quot;,&quot;originating_url&quot;:&quot;https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py&quot;,&quot;user_id&quot;:137187658}}" hydro-click-hmac="a88ec043cf04b6685017b7090c2d452b9d714be73d70ff971108da088be77a2e" id="item-9e452870-4f52-4957-88fd-e8a04901609c" href="https://github.com/issues" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span></a>
  
  
</li>

        
          
<li item_id="password" data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-hotkey="g p" hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py&quot;,&quot;target&quot;:&quot;PULL_REQUESTS&quot;,&quot;originating_url&quot;:&quot;https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py&quot;,&quot;user_id&quot;:137187658}}" hydro-click-hmac="040e0a56714b6575c050251f645ff8fc6deb5aa2f6f969958f05ca6996e6bee1" id="item-0d02fe0a-bdcb-4262-a77c-5258bace83bb" href="https://github.com/pulls" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span></a>
  
  
</li>

        
          
<li item_id="billing" data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py&quot;,&quot;target&quot;:&quot;DISCUSSIONS&quot;,&quot;originating_url&quot;:&quot;https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py&quot;,&quot;user_id&quot;:137187658}}" hydro-click-hmac="af6c0a7128c8959cf026307ba0c498f6f5e4f7661c0f93bb060d3613b5cba70b" id="item-c7d5a632-9fb7-4b4a-aa35-a664ba154b64" href="https://github.com/discussions" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment-discussion">
    <path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Discussions
</span></a>
  
  
</li>

</ul>  </nav-list>
</nav>

      <div data-view-component="true" class="my-3 d-flex flex-justify-center height-full">
        <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</div>
</div>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd d-block pt-0">      <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider mt-0 mb-1"></li>

        <nav aria-label="Additional navigation" data-view-component="true" class="ActionList px-0 flex-1">
  
  <nav-list data-catalyst="">
    <ul data-view-component="true" class="ActionListWrap">
        
          
<li item_id="general" data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py&quot;,&quot;target&quot;:&quot;EXPLORE&quot;,&quot;originating_url&quot;:&quot;https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py&quot;,&quot;user_id&quot;:137187658}}" hydro-click-hmac="57e2e7c47889131429d5259d0f4502700b43ae4a79dfcf3524cd324ceb8c7071" id="item-dc1e31fa-9645-4f47-891e-e0b29ed62692" href="https://github.com/explore" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-telescope">
    <path d="M14.184 1.143v-.001l1.422 2.464a1.75 1.75 0 0 1-.757 2.451L3.104 11.713a1.75 1.75 0 0 1-2.275-.702l-.447-.775a1.75 1.75 0 0 1 .53-2.32L11.682.573a1.748 1.748 0 0 1 2.502.57Zm-4.709 9.32h-.001l2.644 3.863a.75.75 0 1 1-1.238.848l-1.881-2.75v2.826a.75.75 0 0 1-1.5 0v-2.826l-1.881 2.75a.75.75 0 1 1-1.238-.848l2.049-2.992a.746.746 0 0 1 .293-.253l1.809-.87a.749.749 0 0 1 .944.252ZM9.436 3.92h-.001l-4.97 3.39.942 1.63 5.42-2.61Zm3.091-2.108h.001l-1.85 1.26 1.505 2.605 2.016-.97a.247.247 0 0 0 .13-.151.247.247 0 0 0-.022-.199l-1.422-2.464a.253.253 0 0 0-.161-.119.254.254 0 0 0-.197.038ZM1.756 9.157a.25.25 0 0 0-.075.33l.447.775a.25.25 0 0 0 .325.1l1.598-.769-.83-1.436-1.465 1Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Explore
</span></a>
  
  
</li>

        
          
<li item_id="general" data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py&quot;,&quot;target&quot;:&quot;MARKETPLACE&quot;,&quot;originating_url&quot;:&quot;https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py&quot;,&quot;user_id&quot;:137187658}}" hydro-click-hmac="511cc62d271fcdbeaacd496a0dcfb00278ad5bb4560e3054f20da0fddd9778d0" id="item-ebb56af0-bede-4b89-9463-aeb8e62820bd" href="https://github.com/marketplace" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gift">
    <path d="M2 2.75A2.75 2.75 0 0 1 4.75 0c.983 0 1.873.42 2.57 1.232.268.318.497.668.68 1.042.183-.375.411-.725.68-1.044C9.376.42 10.266 0 11.25 0a2.75 2.75 0 0 1 2.45 4h.55c.966 0 1.75.784 1.75 1.75v2c0 .698-.409 1.301-1 1.582v4.918A1.75 1.75 0 0 1 13.25 16H2.75A1.75 1.75 0 0 1 1 14.25V9.332C.409 9.05 0 8.448 0 7.75v-2C0 4.784.784 4 1.75 4h.55c-.192-.375-.3-.8-.3-1.25ZM7.25 9.5H2.5v4.75c0 .138.112.25.25.25h4.5Zm1.5 0v5h4.5a.25.25 0 0 0 .25-.25V9.5Zm0-4V8h5.5a.25.25 0 0 0 .25-.25v-2a.25.25 0 0 0-.25-.25Zm-7 0a.25.25 0 0 0-.25.25v2c0 .138.112.25.25.25h5.5V5.5h-5.5Zm3-4a1.25 1.25 0 0 0 0 2.5h2.309c-.233-.818-.542-1.401-.878-1.793-.43-.502-.915-.707-1.431-.707ZM8.941 4h2.309a1.25 1.25 0 0 0 0-2.5c-.516 0-1 .205-1.43.707-.337.392-.646.975-.879 1.793Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Marketplace
</span></a>
  
  
</li>

        
          
<li item_id="feedback" data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a id="item-6998ce3c-3b06-4d55-b606-1174ba78bd43" href="https://gh.io/navigation-update" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment-discussion">
    <path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Give new navigation feedback
</span>        <span class="ActionListItem-visual ActionListItem-visual--trailing">
          <span title="Beta" data-view-component="true" class="Counter color-bg-default color-border-success-emphasis color-fg-success">Beta</span>
        </span>
</a>
  
  
</li>

</ul>  </nav-list>
</nav>

      <div data-view-component="true" class="px-2">      <p class="color-fg-subtle text-small text-light">© 2023 GitHub, Inc.</p>

      <div data-view-component="true" class="d-flex text-small text-light">
          <a target="_blank" href="https://github.com/about" data-view-component="true" class="no-underline mr-2">About</a>
          <a target="_blank" href="https://github.blog/" data-view-component="true" class="no-underline mr-2">Blog</a>
          <a target="_blank" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="no-underline mr-2">Terms</a>
          <a target="_blank" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="no-underline mr-2">Privacy</a>
          <a target="_blank" href="https://github.com/security" data-view-component="true" class="no-underline mr-2">Security</a>
        <a target="_blank" href="https://www.githubstatus.com/" data-view-component="true" class="no-underline mr-3">Status</a>
</div></div>
</div>
</modal-dialog></div>

  </include-fragment>
</deferred-side-panel>

        <a class="AppHeader-logo ml-2" href="https://github.com/" data-hotkey="g d" aria-label="Homepage " data-turbo="false" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}">
          <svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle color-fg-default">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
        </a>

          <div class="AppHeader-context">
  <div class="AppHeader-context-compact">
        <button aria-expanded="false" aria-haspopup="dialog" aria-label="Page context: PowerstarPrasad / projects_5" id="dialog-show-context-region-dialog" data-show-dialog-id="context-region-dialog" type="button" data-view-component="true" class="AppHeader-context-compact-trigger Truncate Button--secondary Button--medium Button box-shadow-none">    <span class="Button-content">
      <span class="Button-label"><span class="AppHeader-context-compact-lead">
                <span class="AppHeader-context-compact-parentItem">PowerstarPrasad</span>
                <span class="AppHeader-context-compact-separator">&nbsp;/</span>

            </span>

            <strong class="AppHeader-context-compact-mainItem d-flex flex-items-center Truncate">
  <span class="Truncate-text ">projects_5</span>

</strong></span>
    </span>
</button>  

<div class="Overlay--hidden Overlay-backdrop--center" data-modal-dialog-overlay="">
  <modal-dialog role="dialog" id="context-region-dialog" aria-modal="true" aria-disabled="true" aria-describedby="context-region-dialog-title context-region-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="context-region-dialog-title">
        Navigate back to
      </h1>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="context-region-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body">          <ul role="list" class="list-style-none">
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;PowerstarPrasad&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="https://github.com/PowerstarPrasad" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
          PowerstarPrasad
        </span>

</a>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;projects_5&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="https://github.com/PowerstarPrasad/projects_5" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
          projects_5
        </span>

</a>
    </li>
</ul>

</div>
      
</modal-dialog></div>
  </div>

  <div class="AppHeader-context-full">
    <nav role="navigation" aria-label="Page context">
      <ul role="list" class="list-style-none">
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;PowerstarPrasad&quot;,&quot;screen_size&quot;:&quot;full&quot;}" data-hovercard-type="user" data-hovercard-url="/users/PowerstarPrasad/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/PowerstarPrasad" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">
          PowerstarPrasad
        </span>

</a>
        <span class="AppHeader-context-item-separator">/</span>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;projects_5&quot;,&quot;screen_size&quot;:&quot;full&quot;}" href="https://github.com/PowerstarPrasad/projects_5" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">
          projects_5
        </span>

</a>
    </li>
</ul>

    </nav>
  </div>
</div>

      </div>
      <div class="AppHeader-globalBar-end">
          <div class="AppHeader-search">
              


<template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<qbsearch-input class="search-input" data-scope="repo:PowerstarPrasad/projects_5" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="xb4JouCrGs_dyXKQZIZL9twEuHKjbfAqtKUO2Y4DZqlckZWvoOY2mdAkG7dmg_4Yl4ApEHyqUOG7XXSDeytE8A" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="PowerstarPrasad/projects_5" data-current-org="" data-current-owner="PowerstarPrasad" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0" data-action="click:qbsearch-input#searchInputContainerClicked">
      
            <button type="button" data-action="click:qbsearch-input#handleExpand" class="AppHeader-button AppHeader-search-whenNarrow" aria-label="Search or jump to…" aria-expanded="false" aria-haspopup="dialog">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </button>


<div class="AppHeader-search-whenRegular">
  <div class="AppHeader-search-wrap AppHeader-search-wrap--hasTrailing">
    <div class="AppHeader-search-control">
      <label for="AppHeader-searchInput" aria-label="Search or jump to…" class="AppHeader-search-visual--leading">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
      </label>

                <button type="button" data-target="qbsearch-input.inputButton" data-action="click:qbsearch-input#handleExpand" class="AppHeader-searchButton form-control input-contrast text-left color-fg-subtle no-wrap placeholder" data-hotkey="s,/" fdprocessedid="jo8x9r">
            <div class="overflow-hidden">
              <span data-target="qbsearch-input.inputButtonText">
  Type <kbd class="AppHeader-search-kbd">/</kbd> to search
</span>
            </div>
          </button>

    </div>


      <button type="button" id="AppHeader-commandPalette-button" class="AppHeader-search-action--trailing js-activate-command-palette" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;command_palette&quot;,&quot;label&quot;:&quot;open command palette&quot;}" aria-labelledby="tooltip-9916f002-7cb5-4687-9285-6a64c84b3cc8" fdprocessedid="5euhi">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-command-palette">
    <path d="m6.354 8.04-4.773 4.773a.75.75 0 1 0 1.061 1.06L7.945 8.57a.75.75 0 0 0 0-1.06L2.642 2.206a.75.75 0 0 0-1.06 1.061L6.353 8.04ZM8.75 11.5a.75.75 0 0 0 0 1.5h5.5a.75.75 0 0 0 0-1.5h-5.5Z"></path>
</svg>
      </button>

      <tool-tip id="tooltip-9916f002-7cb5-4687-9285-6a64c84b3cc8" for="AppHeader-commandPalette-button" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        position: absolute;
        z-index: 1000000;
        padding: .5em .75em;
        font: normal normal 11px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
        -webkit-font-smoothing: subpixel-antialiased;
        color: var(--color-fg-on-emphasis);
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--color-neutral-emphasis-plus);
        border-radius: 6px;
        opacity: 0;
        max-width: 250px;
        word-wrap: break-word;
        white-space: normal;
        width: max-content;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--color-neutral-emphasis-plus);
        content: "";
        border: 6px solid transparent;
        opacity: 0
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0
        }
        to {
          opacity: 1
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: ""
      }

      :host(.tooltip-open),
      :host(.tooltip-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--color-neutral-emphasis-plus)
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--color-neutral-emphasis-plus)
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%
      }

      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }

      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }

      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--color-neutral-emphasis-plus)
      }

      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--color-neutral-emphasis-plus)
      }
    </style><slot></slot></template>Command palette</tool-tip>
  </div>
</div>

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit" data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;">
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          
  <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>  

      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

        <div class="position-relative">
                <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                    combobox-commit:query-builder#comboboxCommit
                    mousedown:query-builder#resultsMousedown
                  " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results"><li role="presentation" class="ActionList-sectionDivider">
        <ul role="presentation">
          <li role="option" class="ActionListItem" data-type="command-result" id="query-builder-test-result-repo:powerstarprasad/projects_5-" data-value="repo:PowerstarPrasad/projects_5 " data-command-name="blackbird-monolith.search" data-command-payload="{&quot;query&quot;:&quot;repo:PowerstarPrasad/projects_5 &quot;}" aria-label="repo:PowerstarPrasad/projects_5 , Search in this repository">
        <span class="ActionListContent ActionListContent--visual16 QueryBuilder-ListItem">
          <span id="query-builder-test-result-repo:powerstarprasad/projects_5---leading" class="ActionListItem-visual ActionListItem-visual--leading">
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
              </span>
          <span class="ActionListItem-descriptionWrap">
            <span class="ActionListItem-label text-normal"> <span class="">repo:</span><span class="qb-filter-value">PowerstarPrasad/projects_5</span><span class=""> </span> </span>
            
          </span>

          <span aria-hidden="true" class="ActionListItem-description QueryBuilder-ListItem-trailing">Search in this repository</span>
        </span>
      </li><li role="option" class="ActionListItem" data-type="command-result" id="query-builder-test-result-user:powerstarprasad-" data-value="user:PowerstarPrasad " data-command-name="blackbird-monolith.search" data-command-payload="{&quot;query&quot;:&quot;user:PowerstarPrasad &quot;}" aria-label="user:PowerstarPrasad , Search in this owner">
        <span class="ActionListContent ActionListContent--visual16 QueryBuilder-ListItem">
          <span id="query-builder-test-result-user:powerstarprasad---leading" class="ActionListItem-visual ActionListItem-visual--leading">
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
              </span>
          <span class="ActionListItem-descriptionWrap">
            <span class="ActionListItem-label text-normal"> <span class="">user:</span><span class="qb-filter-value">PowerstarPrasad</span><span class=""> </span> </span>
            
          </span>

          <span aria-hidden="true" class="ActionListItem-description QueryBuilder-ListItem-trailing">Search in this owner</span>
        </span>
      </li>
        </ul>
      </li>
                <li aria-hidden="true" class="ActionList-sectionDivider"></li><li role="presentation" class="ActionList-sectionDivider">
        <h3 role="presentation" class="ActionList-sectionDivider-title QueryBuilder-sectionTitle p-2 text-left" aria-hidden="true">
          Owners
        </h3>
        <ul role="presentation">
          <li role="option" class="ActionListItem" data-type="url-result" id="query-builder-test-result-genymobile" data-value="Genymobile" aria-label="Genymobile, jump to this owner">
        <a href="https://github.com/Genymobile" data-action="click:query-builder#navigate" tabindex="-1" class="QueryBuilder-ListItem-link ActionListContent ActionListContent--visual16 QueryBuilder-ListItem">
          <span id="query-builder-test-result-genymobile--leading" class="ActionListItem-visual ActionListItem-visual--leading">
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
              </span>
          <span class="ActionListItem-descriptionWrap">
            <span class="ActionListItem-label text-normal"> <span class="">Genymobile</span> </span>
            
          </span>

          <span aria-hidden="true" class="ActionListItem-description QueryBuilder-ListItem-trailing">Jump to</span>
        </a>
      </li><li role="option" class="ActionListItem" data-type="url-result" id="query-builder-test-result-git-guides" data-value="git-guides" aria-label="git-guides, jump to this owner">
        <a href="https://github.com/git-guides" data-action="click:query-builder#navigate" tabindex="-1" class="QueryBuilder-ListItem-link ActionListContent ActionListContent--visual16 QueryBuilder-ListItem">
          <span id="query-builder-test-result-git-guides--leading" class="ActionListItem-visual ActionListItem-visual--leading">
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
              </span>
          <span class="ActionListItem-descriptionWrap">
            <span class="ActionListItem-label text-normal"> <span class="">git-guides</span> </span>
            
          </span>

          <span aria-hidden="true" class="ActionListItem-description QueryBuilder-ListItem-trailing">Jump to</span>
        </a>
      </li><li role="option" class="ActionListItem" data-type="url-result" id="query-builder-test-result-venkatesh-gorrela" data-value="venkatesh-gorrela" aria-label="venkatesh-gorrela, jump to this owner">
        <a href="https://github.com/venkatesh-gorrela" data-action="click:query-builder#navigate" tabindex="-1" class="QueryBuilder-ListItem-link ActionListContent ActionListContent--visual16 QueryBuilder-ListItem">
          <span id="query-builder-test-result-venkatesh-gorrela--leading" class="ActionListItem-visual ActionListItem-visual--leading">
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
              </span>
          <span class="ActionListItem-descriptionWrap">
            <span class="ActionListItem-label text-normal"> <span class="">venkatesh-gorrela</span> </span>
            
          </span>

          <span aria-hidden="true" class="ActionListItem-description QueryBuilder-ListItem-trailing">Jump to</span>
        </a>
      </li><li role="option" class="ActionListItem" data-type="url-result" id="query-builder-test-result-powerstarprasad" data-value="PowerstarPrasad" aria-label="PowerstarPrasad, jump to this owner">
        <a href="https://github.com/PowerstarPrasad" data-action="click:query-builder#navigate" tabindex="-1" class="QueryBuilder-ListItem-link ActionListContent ActionListContent--visual16 QueryBuilder-ListItem">
          <span id="query-builder-test-result-powerstarprasad--leading" class="ActionListItem-visual ActionListItem-visual--leading">
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
              </span>
          <span class="ActionListItem-descriptionWrap">
            <span class="ActionListItem-label text-normal"> <span class="">PowerstarPrasad</span> </span>
            
          </span>

          <span aria-hidden="true" class="ActionListItem-description QueryBuilder-ListItem-trailing">Jump to</span>
        </a>
      </li>
        </ul>
      </li>
                <li aria-hidden="true" class="ActionList-sectionDivider"></li><li role="presentation" class="ActionList-sectionDivider">
        <h3 role="presentation" class="ActionList-sectionDivider-title QueryBuilder-sectionTitle p-2 text-left" aria-hidden="true">
          Repositories
        </h3>
        <ul role="presentation">
          <li role="option" class="ActionListItem" data-type="url-result" id="query-builder-test-result-genymobile/scrcpy" data-value="Genymobile/scrcpy" aria-label="Genymobile/scrcpy, jump to this repository">
        <a href="https://github.com/Genymobile/scrcpy" data-action="click:query-builder#navigate" tabindex="-1" class="QueryBuilder-ListItem-link ActionListContent ActionListContent--visual16 QueryBuilder-ListItem">
          <span id="query-builder-test-result-genymobile/scrcpy--leading" class="ActionListItem-visual ActionListItem-visual--leading">
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
              </span>
          <span class="ActionListItem-descriptionWrap">
            <span class="ActionListItem-label text-normal"> <span class="">Genymobile/scrcpy</span> </span>
            
          </span>

          <span aria-hidden="true" class="ActionListItem-description QueryBuilder-ListItem-trailing">Jump to</span>
        </a>
      </li><li role="option" class="ActionListItem" data-type="url-result" id="query-builder-test-result-git-guides/install-git" data-value="git-guides/install-git" aria-label="git-guides/install-git, jump to this repository">
        <a href="https://github.com/git-guides/install-git" data-action="click:query-builder#navigate" tabindex="-1" class="QueryBuilder-ListItem-link ActionListContent ActionListContent--visual16 QueryBuilder-ListItem">
          <span id="query-builder-test-result-git-guides/install-git--leading" class="ActionListItem-visual ActionListItem-visual--leading">
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
              </span>
          <span class="ActionListItem-descriptionWrap">
            <span class="ActionListItem-label text-normal"> <span class="">git-guides/install-git</span> </span>
            
          </span>

          <span aria-hidden="true" class="ActionListItem-description QueryBuilder-ListItem-trailing">Jump to</span>
        </a>
      </li><li role="option" class="ActionListItem" data-type="url-result" id="query-builder-test-result-venkatesh-gorrela/projects_5" data-value="venkatesh-gorrela/projects_5" aria-label="venkatesh-gorrela/projects_5, jump to this repository">
        <a href="https://github.com/venkatesh-gorrela/projects_5" data-action="click:query-builder#navigate" tabindex="-1" class="QueryBuilder-ListItem-link ActionListContent ActionListContent--visual16 QueryBuilder-ListItem">
          <span id="query-builder-test-result-venkatesh-gorrela/projects_5--leading" class="ActionListItem-visual ActionListItem-visual--leading">
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
              </span>
          <span class="ActionListItem-descriptionWrap">
            <span class="ActionListItem-label text-normal"> <span class="">venkatesh-gorrela/projects_5</span> </span>
            
          </span>

          <span aria-hidden="true" class="ActionListItem-description QueryBuilder-ListItem-trailing">Jump to</span>
        </a>
      </li><li role="option" class="ActionListItem" data-type="url-result" id="query-builder-test-result-powerstarprasad/gangaprasad" data-value="PowerstarPrasad/gangaprasad" aria-label="PowerstarPrasad/gangaprasad, jump to this repository">
        <a href="https://github.com/PowerstarPrasad/gangaprasad" data-action="click:query-builder#navigate" tabindex="-1" class="QueryBuilder-ListItem-link ActionListContent ActionListContent--visual16 QueryBuilder-ListItem">
          <span id="query-builder-test-result-powerstarprasad/gangaprasad--leading" class="ActionListItem-visual ActionListItem-visual--leading">
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
              </span>
          <span class="ActionListItem-descriptionWrap">
            <span class="ActionListItem-label text-normal"> <span class="">PowerstarPrasad/gangaprasad</span> </span>
            
          </span>

          <span aria-hidden="true" class="ActionListItem-description QueryBuilder-ListItem-trailing">Jump to</span>
        </a>
      </li><li role="option" class="ActionListItem" data-type="url-result" id="query-builder-test-result-powerstarprasad/powerstarprasad" data-value="PowerstarPrasad/PowerstarPrasad" aria-label="PowerstarPrasad/PowerstarPrasad, jump to this repository">
        <a href="https://github.com/PowerstarPrasad/PowerstarPrasad" data-action="click:query-builder#navigate" tabindex="-1" class="QueryBuilder-ListItem-link ActionListContent ActionListContent--visual16 QueryBuilder-ListItem">
          <span id="query-builder-test-result-powerstarprasad/powerstarprasad--leading" class="ActionListItem-visual ActionListItem-visual--leading">
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
              </span>
          <span class="ActionListItem-descriptionWrap">
            <span class="ActionListItem-label text-normal"> <span class="">PowerstarPrasad/PowerstarPrasad</span> </span>
            
          </span>

          <span aria-hidden="true" class="ActionListItem-description QueryBuilder-ListItem-trailing">Jump to</span>
        </a>
      </li>
        </ul>
      </li></ul>
        </div>
    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only">11 suggestions.</div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="color-fg-accent text-normal ml-2">
              Search syntax tips
</a>            <div class="d-flex flex-1"></div>
              <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">    <span class="Button-content">
      <span class="Button-label">Give feedback</span>
    </span>
</button>  
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed width-full" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<div class="Overlay--hidden Overlay-backdrop--center" data-modal-dialog-overlay="">
  <modal-dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" role="dialog" id="feedback-dialog" aria-modal="true" aria-disabled="true" aria-describedby="feedback-dialog-title feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="3ORL5NubybCKJ4BEClEJ99GaSTQd0h3kk9nLZxDMYVSjfg0FYbGwsYKOYyz8_cQyzf_zeC3RG-5qv-9k2jVbig">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</modal-dialog></div>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<div class="Overlay--hidden Overlay-backdrop--center" data-modal-dialog-overlay="">
  <modal-dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" role="dialog" id="custom-scopes-dialog" aria-modal="true" aria-disabled="true" aria-describedby="custom-scopes-dialog-title custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="8I5-7gGB6v74sgvz-h9svHFEUTPenVYNLgVBqfskdaCH0G3FxL94V0ev1tkG8RIpP5eKN4gbf6rZFEc0GLt2nQ">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false">
              <input type="hidden" value="wZ-juEnBufFfTSjbV3Bt5JyVN1vE-x4Se3zL8968l1ueXint3m9mNndg9p62heHh3fuKUm1G_UOlCMjODSBKPw" data-csrf="true">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a href="https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</modal-dialog></div>
    </custom-scopes>
  </div>
</qbsearch-input><input type="hidden" value="3QLl4Re-RDFm--HKnR66Z2pQPCNUZu1pTaxgA7r34jPCHmG9swjtnEtbLZdEAv_ZU_FM8MmKbGVbp_gL2bq68w" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf">

          </div>

        <div class="AppHeader-actions">
          <action-menu data-select-variant="none" data-view-component="true" data-catalyst="">
  <focus-group direction="vertical" mnemonics="" retain="">
    <div data-view-component="true" class="Button-withTooltip">  <button id="global-create-menu-button" popovertarget="global-create-menu-overlay" aria-label="Create something new" aria-controls="global-create-menu-list" aria-haspopup="true" type="button" data-view-component="true" class="AppHeader-button Button--secondary Button--small Button width-auto color-fg-muted box-shadow-none" aria-describedby="tooltip-949bf178-e6de-4c06-b8dc-97938e34b3de" fdprocessedid="8jpftd">    <span class="Button-content">
        <span class="Button-visual Button-leadingVisual">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
        </span>
      <span class="Button-label"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg></span>
    </span>
</button>  <tool-tip id="tooltip-949bf178-e6de-4c06-b8dc-97938e34b3de" for="global-create-menu-button" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        position: absolute;
        z-index: 1000000;
        padding: .5em .75em;
        font: normal normal 11px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
        -webkit-font-smoothing: subpixel-antialiased;
        color: var(--color-fg-on-emphasis);
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--color-neutral-emphasis-plus);
        border-radius: 6px;
        opacity: 0;
        max-width: 250px;
        word-wrap: break-word;
        white-space: normal;
        width: max-content;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--color-neutral-emphasis-plus);
        content: "";
        border: 6px solid transparent;
        opacity: 0
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0
        }
        to {
          opacity: 1
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: ""
      }

      :host(.tooltip-open),
      :host(.tooltip-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--color-neutral-emphasis-plus)
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--color-neutral-emphasis-plus)
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%
      }

      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }

      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }

      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--color-neutral-emphasis-plus)
      }

      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--color-neutral-emphasis-plus)
      }
    </style><slot></slot></template>Create new...</tool-tip>
</div>

<anchored-position id="global-create-menu-overlay" anchor="global-create-menu-button" align="end" side="outside-bottom" anchor-offset="normal" popover="auto" aria-label="Menu" data-view-component="true" class="Overlay Overlay--size-auto Overlay--anchorAlign-end Overlay--anchorSide-outside-bottom" style="top: 52px; left: 1343.2px;">
  
    
        <div data-view-component="true">
  <ul aria-labelledby="global-create-menu-button" id="global-create-menu-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new repository&quot;}" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/new" tabindex="-1" id="item-a2316fb5-8799-4199-818c-e36b67bdd92a" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
              New repository

</span></a>
  
  
</li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;import repository&quot;}" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/new/import" tabindex="-1" id="item-f9c0dcbe-255e-4acc-a877-2e64ad729896" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-push">
    <path d="M1 2.5A2.5 2.5 0 0 1 3.5 0h8.75a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0V1.5h-8a1 1 0 0 0-1 1v6.708A2.493 2.493 0 0 1 3.5 9h3.25a.75.75 0 0 1 0 1.5H3.5a1 1 0 0 0 0 2h5.75a.75.75 0 0 1 0 1.5H3.5A2.5 2.5 0 0 1 1 11.5Zm13.23 7.79h-.001l-1.224-1.224v6.184a.75.75 0 0 1-1.5 0V9.066L10.28 10.29a.75.75 0 0 1-1.06-1.061l2.505-2.504a.75.75 0 0 1 1.06 0L15.29 9.23a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                Import repository

</span></a>
  
  
</li>
      <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new codespace&quot;}" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/codespaces/new" tabindex="-1" id="item-abd1c6ac-7104-4c88-b897-51c36d824873" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New codespace

</span></a>
  
  
</li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new gist&quot;}" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://gist.github.com/" tabindex="-1" id="item-30cb7865-029d-4503-b191-c5b6406f44ad" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
              New gist

</span></a>
  
  
</li>
      <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new organization&quot;}" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/account/organizations/new" tabindex="-1" id="item-0e926d22-1ee6-4efe-9291-4eb97d64f1f2" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-organization">
    <path d="M1.75 16A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0h8.5C11.216 0 12 .784 12 1.75v12.5c0 .085-.006.168-.018.25h2.268a.25.25 0 0 0 .25-.25V8.285a.25.25 0 0 0-.111-.208l-1.055-.703a.749.749 0 1 1 .832-1.248l1.055.703c.487.325.779.871.779 1.456v5.965A1.75 1.75 0 0 1 14.25 16h-3.5a.766.766 0 0 1-.197-.026c-.099.017-.2.026-.303.026h-3a.75.75 0 0 1-.75-.75V14h-1v1.25a.75.75 0 0 1-.75.75Zm-.25-1.75c0 .138.112.25.25.25H4v-1.25a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 .75.75v1.25h2.25a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25ZM3.75 6h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 3.75A.75.75 0 0 1 3.75 3h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 3.75Zm4 3A.75.75 0 0 1 7.75 6h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 7 6.75ZM7.75 3h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 9.75A.75.75 0 0 1 3.75 9h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 9.75ZM7.75 9h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New organization

</span></a>
  
  
</li>
</ul>  
</div>

</anchored-position>  </focus-group>
</action-menu>

          <div data-view-component="true" class="Button-withTooltip">
  <a href="https://github.com/issues" id="icon-button-6df920b0-1905-4bb0-898e-a993d38e1778" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted" aria-labelledby="tooltip-12853b06-e572-4f45-acaa-6b0283c33b62">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened Button-visual">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
</a>  <tool-tip id="tooltip-12853b06-e572-4f45-acaa-6b0283c33b62" for="icon-button-6df920b0-1905-4bb0-898e-a993d38e1778" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        position: absolute;
        z-index: 1000000;
        padding: .5em .75em;
        font: normal normal 11px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
        -webkit-font-smoothing: subpixel-antialiased;
        color: var(--color-fg-on-emphasis);
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--color-neutral-emphasis-plus);
        border-radius: 6px;
        opacity: 0;
        max-width: 250px;
        word-wrap: break-word;
        white-space: normal;
        width: max-content;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--color-neutral-emphasis-plus);
        content: "";
        border: 6px solid transparent;
        opacity: 0
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0
        }
        to {
          opacity: 1
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: ""
      }

      :host(.tooltip-open),
      :host(.tooltip-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--color-neutral-emphasis-plus)
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--color-neutral-emphasis-plus)
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%
      }

      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }

      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }

      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--color-neutral-emphasis-plus)
      }

      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--color-neutral-emphasis-plus)
      }
    </style><slot></slot></template>Issues</tool-tip>
</div>
          <div data-view-component="true" class="Button-withTooltip">
  <a href="https://github.com/pulls" id="icon-button-6e1183e7-21bf-4ef8-9e21-301aeee88bfb" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted" aria-labelledby="tooltip-cad18d2d-0389-403d-9935-9cb4f6da3cb8">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request Button-visual">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
</a>  <tool-tip id="tooltip-cad18d2d-0389-403d-9935-9cb4f6da3cb8" for="icon-button-6e1183e7-21bf-4ef8-9e21-301aeee88bfb" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        position: absolute;
        z-index: 1000000;
        padding: .5em .75em;
        font: normal normal 11px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
        -webkit-font-smoothing: subpixel-antialiased;
        color: var(--color-fg-on-emphasis);
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--color-neutral-emphasis-plus);
        border-radius: 6px;
        opacity: 0;
        max-width: 250px;
        word-wrap: break-word;
        white-space: normal;
        width: max-content;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--color-neutral-emphasis-plus);
        content: "";
        border: 6px solid transparent;
        opacity: 0
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0
        }
        to {
          opacity: 1
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: ""
      }

      :host(.tooltip-open),
      :host(.tooltip-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--color-neutral-emphasis-plus)
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--color-neutral-emphasis-plus)
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%
      }

      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }

      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }

      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--color-neutral-emphasis-plus)
      }

      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--color-neutral-emphasis-plus)
      }
    </style><slot></slot></template>Pull requests</tool-tip>
</div>
        </div>

        <div class="mr-0">
          

<notification-indicator data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTM3MTg3NjU4IiwidCI6MTY4NzI3MjA0OX0=--9c6a4893963ecbf76bf69beefda6e2f82280c0227f11ff4e547b6cbee5d8dbe1" data-indicator-mode="none" data-tooltip-global="You have unread notifications" data-tooltip-unavailable="Notifications are unavailable at the moment." data-tooltip-none="You have no unread notifications" data-header-redesign-enabled="true" data-fetch-indicator-src="/notifications/indicator" data-fetch-indicator-enabled="true" data-view-component="true" class="js-socket-channel" data-fetch-retry-delay-time="500" data-catalyst="">
  <a id="AppHeader-notifications-button" href="https://github.com/notifications" class="AppHeader-button" style="width:32px;height:32px;" data-hotkey="g n" data-target="notification-indicator.link" aria-label="Notifications" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;notifications&quot;,&quot;label&quot;:&quot;icon:read&quot;}" aria-describedby="tooltip-d841a2dc-d3c1-4fcd-afdb-7ab198e35b48">

    <span data-target="notification-indicator.badge" class="mail-status unread d-none" hidden="">
    </span>

      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-inbox color-fg-muted mr-0">
    <path d="M2.8 2.06A1.75 1.75 0 0 1 4.41 1h7.18c.7 0 1.333.417 1.61 1.06l2.74 6.395c.04.093.06.194.06.295v4.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25v-4.5c0-.101.02-.202.06-.295Zm1.61.44a.25.25 0 0 0-.23.152L1.887 8H4.75a.75.75 0 0 1 .6.3L6.625 10h2.75l1.275-1.7a.75.75 0 0 1 .6-.3h2.863L11.82 2.652a.25.25 0 0 0-.23-.152Zm10.09 7h-2.875l-1.275 1.7a.75.75 0 0 1-.6.3h-3.5a.75.75 0 0 1-.6-.3L4.375 9.5H1.5v3.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Z"></path>
</svg>
  </a>

    <tool-tip data-target="notification-indicator.tooltip" id="tooltip-d841a2dc-d3c1-4fcd-afdb-7ab198e35b48" for="AppHeader-notifications-button" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        position: absolute;
        z-index: 1000000;
        padding: .5em .75em;
        font: normal normal 11px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
        -webkit-font-smoothing: subpixel-antialiased;
        color: var(--color-fg-on-emphasis);
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--color-neutral-emphasis-plus);
        border-radius: 6px;
        opacity: 0;
        max-width: 250px;
        word-wrap: break-word;
        white-space: normal;
        width: max-content;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--color-neutral-emphasis-plus);
        content: "";
        border: 6px solid transparent;
        opacity: 0
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0
        }
        to {
          opacity: 1
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: ""
      }

      :host(.tooltip-open),
      :host(.tooltip-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--color-neutral-emphasis-plus)
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--color-neutral-emphasis-plus)
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%
      }

      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }

      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }

      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--color-neutral-emphasis-plus)
      }

      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--color-neutral-emphasis-plus)
      }
    </style><slot></slot></template>You have no unread notifications</tool-tip>
</notification-indicator>
        </div>

        

        <div class="AppHeader-user">
          <deferred-side-panel data-url="/_side-panels/user?memex_enabled=true&amp;repository=projects_5&amp;user=PowerstarPrasad&amp;user_can_create_organizations=true&amp;user_id=137187658" data-catalyst="">
  <include-fragment data-target="deferred-side-panel.fragment"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
      <user-drawer-side-panel data-catalyst="">
      <button aria-label="Open user account menu" data-action="click:deferred-side-panel#loadPanel click:deferred-side-panel#panelOpened" data-show-dialog-id="dialog-b56083f0-58b3-4531-a89d-7219288d8b57" id="dialog-show-dialog-b56083f0-58b3-4531-a89d-7219288d8b57" type="button" data-view-component="true" class="AppHeader-logo Button--invisible Button--medium Button Button--invisible-noVisuals color-bg-transparent p-0" fdprocessedid="xfjibd">    <span class="Button-content">
      <span class="Button-label"><img src="./lordtiru_bankproject_files/137187658" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle"></span>
    </span>
</button>  

<div class="Overlay--hidden Overlay-backdrop--side Overlay-backdrop--placement-right" data-modal-dialog-overlay="">
  <modal-dialog data-target="deferred-side-panel.panel" role="dialog" id="dialog-b56083f0-58b3-4531-a89d-7219288d8b57" aria-modal="true" aria-disabled="true" aria-describedby="dialog-b56083f0-58b3-4531-a89d-7219288d8b57-title dialog-b56083f0-58b3-4531-a89d-7219288d8b57-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade SidePanel" style="max-height: 714px;">
    <div styles="flex-direction: row;" data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="dialog-b56083f0-58b3-4531-a89d-7219288d8b57-title">
        Account menu
      </h1>
            <div data-view-component="true" class="d-flex">
      <div data-view-component="true" class="AppHeader-logo position-relative">
        <img src="./lordtiru_bankproject_files/137187658" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle">
</div>        <div data-view-component="true" class="d-flex width-full">        <div data-view-component="true" class="lh-condensed d-flex flex-column flex-justify-center ml-2 f5 mr-auto">
          <span data-view-component="true" class="Truncate d-block text-bold">
    <span data-view-component="true" class="Truncate-text">
            PowerstarPrasad
</span>
</span>          </div>
</div>
</div>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="dialog-b56083f0-58b3-4531-a89d-7219288d8b57" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body d-flex flex-column height-full px-2">      <nav aria-label="User navigation" data-view-component="true" class="ActionList">
  
  <nav-list data-catalyst="">
    <ul data-view-component="true" class="ActionListWrap">
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-1aaa1dca-46ec-43d9-844c-ebd39d1fdae7" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a id="item-0d305ef9-0411-4bdf-a8a1-3414c2c78e7d" href="https://github.com/PowerstarPrasad" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-person">
    <path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6.004 6.004 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0ZM10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your profile
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a id="item-834fb584-b242-4e7d-90f8-7c79b87c80cd" href="https://github.com/PowerstarPrasad?tab=repositories" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your repositories
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a id="item-64dae4f1-cc2b-4b78-a791-c80c8901fa91" href="https://github.com/PowerstarPrasad?tab=projects" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project">
    <path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0ZM1.5 1.75v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25ZM11.75 3a.75.75 0 0 1 .75.75v7.5a.75.75 0 0 1-1.5 0v-7.5a.75.75 0 0 1 .75-.75Zm-8.25.75a.75.75 0 0 1 1.5 0v5.5a.75.75 0 0 1-1.5 0ZM8 3a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 3Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your projects
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a id="item-00ca20f1-3f90-4f13-bc97-3aa84dba0421" href="https://github.com/codespaces" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your codespaces
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-9570fe4a-1aa8-4040-ada6-2d5eafbb52d8" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a id="item-2fd71928-2f96-44a2-a30b-27dba49fb634" href="https://github.com/PowerstarPrasad?tab=stars" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your stars
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a id="item-c309da28-a023-4eef-a679-c80d17514322" href="https://github.com/sponsors/accounts" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-heart">
    <path d="m8 14.25.345.666a.75.75 0 0 1-.69 0l-.008-.004-.018-.01a7.152 7.152 0 0 1-.31-.17 22.055 22.055 0 0 1-3.434-2.414C2.045 10.731 0 8.35 0 5.5 0 2.836 2.086 1 4.25 1 5.797 1 7.153 1.802 8 3.02 8.847 1.802 10.203 1 11.75 1 13.914 1 16 2.836 16 5.5c0 2.85-2.045 5.231-3.885 6.818a22.066 22.066 0 0 1-3.744 2.584l-.018.01-.006.003h-.002ZM4.25 2.5c-1.336 0-2.75 1.164-2.75 3 0 2.15 1.58 4.144 3.365 5.682A20.58 20.58 0 0 0 8 13.393a20.58 20.58 0 0 0 3.135-2.211C12.92 9.644 14.5 7.65 14.5 5.5c0-1.836-1.414-3-2.75-3-1.373 0-2.609.986-3.029 2.456a.749.749 0 0 1-1.442 0C6.859 3.486 5.623 2.5 4.25 2.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your sponsors
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a id="item-0284f791-c679-4ea0-ab09-f339c415212c" href="https://gist.github.com/mine" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code-square">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25Zm7.47 3.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L10.69 8 9.22 6.53a.75.75 0 0 1 0-1.06ZM6.78 6.53 5.31 8l1.47 1.47a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your gists
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-49a7f1ae-5739-4536-97e6-44cb5dc49830" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-cb821df9-a421-4dfd-b24b-51dab69fe1ca" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-25afd7b7-7bab-45b1-90be-551caaf4cec0" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a id="item-ffa57fb7-ff71-4531-b399-5671dc57cb77" href="https://github.com/settings/profile" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gear">
    <path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Settings
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a id="item-eb990ebc-1ece-4286-8431-2095dfac0f15" href="https://docs.github.com/" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          GitHub Docs
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a id="item-fe66b587-4617-4395-909f-327c2c0abcc8" href="https://support.github.com/" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-people">
    <path d="M2 5.5a3.5 3.5 0 1 1 5.898 2.549 5.508 5.508 0 0 1 3.034 4.084.75.75 0 1 1-1.482.235 4 4 0 0 0-7.9 0 .75.75 0 0 1-1.482-.236A5.507 5.507 0 0 1 3.102 8.05 3.493 3.493 0 0 1 2 5.5ZM11 4a3.001 3.001 0 0 1 2.22 5.018 5.01 5.01 0 0 1 2.56 3.012.749.749 0 0 1-.885.954.752.752 0 0 1-.549-.514 3.507 3.507 0 0 0-2.522-2.372.75.75 0 0 1-.574-.73v-.352a.75.75 0 0 1 .416-.672A1.5 1.5 0 0 0 11 5.5.75.75 0 0 1 11 4Zm-5.5-.5a2 2 0 1 0-.001 3.999A2 2 0 0 0 5.5 3.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          GitHub Support
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a id="item-96f6793f-a339-4d27-950b-a496f1396966" href="https://github.com/logout" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          Sign out
</span></a>
  
  
</li>

</ul>  </nav-list>
</nav>


</div>
      
</modal-dialog></div>
  </user-drawer-side-panel>

  </include-fragment>
</deferred-side-panel>
        </div>
      </div>
    </div>


      <div class="AppHeader-localBar">
        <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="https://github.com/PowerstarPrasad/projects_5" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments /PowerstarPrasad/projects_5" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected" aria-current="page">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="https://github.com/PowerstarPrasad/projects_5/pulls" data-tab-item="i1pull-requests-tab" data-selected-links="repo_pulls checks /PowerstarPrasad/projects_5/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="https://github.com/PowerstarPrasad/projects_5/actions" data-tab-item="i2actions-tab" data-selected-links="repo_actions /PowerstarPrasad/projects_5/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="https://github.com/PowerstarPrasad/projects_5/projects" data-tab-item="i3projects-tab" data-selected-links="repo_projects new_repo_project repo_project /PowerstarPrasad/projects_5/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="wiki-tab" href="https://github.com/PowerstarPrasad/projects_5/wiki" data-tab-item="i4wiki-tab" data-selected-links="repo_wiki /PowerstarPrasad/projects_5/wiki" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g w" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Wiki&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
        <span data-content="Wiki">Wiki</span>
          <span id="wiki-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="https://github.com/PowerstarPrasad/projects_5/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /PowerstarPrasad/projects_5/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          

    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="https://github.com/PowerstarPrasad/projects_5/pulse" data-tab-item="i6insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /PowerstarPrasad/projects_5/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="settings-tab" href="https://github.com/PowerstarPrasad/projects_5/settings" data-tab-item="i7settings-tab" data-selected-links="code_review_limits codespaces_repository_settings collaborators custom_tabs hooks integration_installations interaction_limits issue_template_editor key_links_settings notifications repo_actions_settings repo_announcements repo_branch_settings repo_keys_settings repo_pages_settings repo_rule_insights repo_rulesets repo_protected_tags_settings repo_settings reported_content repo_custom_properties repository_actions_settings_add_new_runner repository_actions_settings_general repository_actions_settings_runners repository_environments role_details secrets secrets_settings_actions secrets_settings_codespaces secrets_settings_dependabot security_analysis /PowerstarPrasad/projects_5/settings" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Settings&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gear UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path>
</svg>
        <span data-content="Settings">Settings</span>
          <span id="settings-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">        <details data-view-component="true" class="details-overlay details-reset position-relative">
    <summary role="button" data-view-component="true" aria-haspopup="menu">          <div class="UnderlineNav-item mr-0 border-0">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
            <span class="sr-only">More</span>
          </div>
</summary>
    <details-menu role="menu" data-view-component="true" class="dropdown-menu dropdown-menu-sw" data-focus-trap="active"><span class="sentinel" tabindex="0" aria-hidden="true"></span>          <ul>
              <li data-menu-item="i0code-tab" hidden="">
                <a role="menuitem" class="js-selected-navigation-item dropdown-item selected" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments /PowerstarPrasad/projects_5" href="https://github.com/PowerstarPrasad/projects_5" aria-current="page">
                  Code
</a>              </li>
              <li data-menu-item="i1pull-requests-tab" hidden="">
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_pulls checks /PowerstarPrasad/projects_5/pulls" href="https://github.com/PowerstarPrasad/projects_5/pulls">
                  Pull requests
</a>              </li>
              <li data-menu-item="i2actions-tab" hidden="">
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_actions /PowerstarPrasad/projects_5/actions" href="https://github.com/PowerstarPrasad/projects_5/actions">
                  Actions
</a>              </li>
              <li data-menu-item="i3projects-tab" hidden="">
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_projects new_repo_project repo_project /PowerstarPrasad/projects_5/projects" href="https://github.com/PowerstarPrasad/projects_5/projects">
                  Projects
</a>              </li>
              <li data-menu-item="i4wiki-tab" hidden="">
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_wiki /PowerstarPrasad/projects_5/wiki" href="https://github.com/PowerstarPrasad/projects_5/wiki">
                  Wiki
</a>              </li>
              <li data-menu-item="i5security-tab" hidden="">
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="security overview alerts policy token_scanning code_scanning /PowerstarPrasad/projects_5/security" href="https://github.com/PowerstarPrasad/projects_5/security">
                  Security
</a>              </li>
              <li data-menu-item="i6insights-tab" hidden="">
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /PowerstarPrasad/projects_5/pulse" href="https://github.com/PowerstarPrasad/projects_5/pulse">
                  Insights
</a>              </li>
              <li data-menu-item="i7settings-tab" hidden="">
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="code_review_limits codespaces_repository_settings collaborators custom_tabs hooks integration_installations interaction_limits issue_template_editor key_links_settings notifications repo_actions_settings repo_announcements repo_branch_settings repo_keys_settings repo_pages_settings repo_rule_insights repo_rulesets repo_protected_tags_settings repo_settings reported_content repo_custom_properties repository_actions_settings_add_new_runner repository_actions_settings_general repository_actions_settings_runners repository_environments role_details secrets secrets_settings_actions secrets_settings_codespaces secrets_settings_dependabot security_analysis /PowerstarPrasad/projects_5/settings" href="https://github.com/PowerstarPrasad/projects_5/settings">
                  Settings
</a>              </li>
          </ul>
<span class="sentinel" tabindex="0" aria-hidden="true"></span></details-menu>
</details></div>
</nav>
      </div>
</header>


      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash flash flash-warn mb-3">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a href="https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a href="https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden="">You switched accounts on another tab or window. <a href="https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py">Reload</a> to refresh your session.</span>

    <button class="flash-close js-flash-close" type="button" aria-label="Close">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>

  
</div>
          
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" data-turbo-replace="">





  <template class="js-flash-template"></template>
</div>


    
    <notification-shelf-watcher data-base-url="https://github.com/notifications/beta/shelf" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTM3MTg3NjU4IiwidCI6MTY4NzI3MjA0OX0=--9c6a4893963ecbf76bf69beefda6e2f82280c0227f11ff4e547b6cbee5d8dbe1" data-view-component="true" class="js-socket-channel" data-refresh-delay="500" data-catalyst=""></notification-shelf-watcher>
  <div hidden="" data-initial="" data-target="notification-shelf-watcher.placeholder"></div>






      <details class="details-reset details-overlay details-overlay-dark js-command-palette-dialog" id="command-palette-pjax-container" data-turbo-replace="">
  <summary aria-label="command palette trigger" tabindex="-1" role="button"></summary>
  <details-dialog class="command-palette-details-dialog d-flex flex-column flex-justify-center height-fit" aria-label="command palette" role="dialog" aria-modal="true">
    <command-palette class="command-palette color-bg-default rounded-3 border color-shadow-small" return-to="/PowerstarPrasad/projects_5/blob/main/railway%20project.py" user-id="137187658" activation-hotkey="Mod+k,Mod+Alt+k" command-mode-hotkey="Mod+Shift+k" data-action="
        command-palette-input-ready:command-palette#inputReady
        command-palette-page-stack-updated:command-palette#updateInputScope
        itemsUpdated:command-palette#itemsUpdated
        keydown:command-palette#onKeydown
        loadingStateChanged:command-palette#loadingStateChanged
        selectedItemChanged:command-palette#selectedItemChanged
        pageFetchError:command-palette#pageFetchError
      " data-catalyst="">

        <command-palette-mode data-char="#" data-scope-types="[&quot;&quot;]" data-placeholder="Search issues and pull requests" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="#" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-placeholder="Search issues, pull requests, discussions, and projects" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="!" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-placeholder="Search projects" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="@" data-scope-types="[&quot;&quot;]" data-placeholder="Search or jump to a user, organization, or repository" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="@" data-scope-types="[&quot;owner&quot;]" data-placeholder="Search or jump to a repository" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="/" data-scope-types="[&quot;repository&quot;]" data-placeholder="Search files" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="?" data-placeholder="" data-catalyst="" data-scope-types=""></command-palette-mode>
        <command-palette-mode data-char="&gt;" data-placeholder="Run a command" data-scope-types="" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="" data-scope-types="[&quot;&quot;]" data-placeholder="Search or jump to..." data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="" data-scope-types="[&quot;owner&quot;]" data-placeholder="Search or jump to..." data-catalyst=""></command-palette-mode>
      <command-palette-mode class="js-command-palette-default-mode" data-char="" data-placeholder="Search or jump to..." data-scope-types="" data-catalyst=""></command-palette-mode>

      <command-palette-input placeholder="Search or jump to..." data-action="
          command-palette-input:command-palette#onInput
          command-palette-select:command-palette#onSelect
          command-palette-descope:command-palette#onDescope
          command-palette-cleared:command-palette#onInputClear
        " data-catalyst="" class="d-flex flex-items-center flex-nowrap py-1 pl-3 pr-2 border-bottom">
        <div class="js-search-icon d-flex flex-items-center mr-2" style="height: 26px">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search color-fg-muted">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
        </div>
        <div class="js-spinner d-flex flex-items-center mr-2 color-fg-muted" hidden="">
          <svg aria-label="Loading" class="anim-rotate" viewBox="0 0 16 16" fill="none" width="16" height="16">
            <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
            <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
          </svg>
        </div>
        <command-palette-scope data-catalyst="" class="d-inline-flex">
          <div data-target="command-palette-scope.placeholder" hidden="" class="color-fg-subtle">/&nbsp;&nbsp;<span class="text-semibold color-fg-default">...</span>&nbsp;&nbsp;/&nbsp;&nbsp;</div>
              <command-palette-token data-text="PowerstarPrasad" data-id="U_kgDOCC1RSg" data-type="owner" data-value="PowerstarPrasad" data-targets="command-palette-scope.tokens" class="color-fg-default text-semibold" style="white-space:nowrap;line-height:20px;" id="" data-catalyst="">PowerstarPrasad<span class="color-fg-subtle text-normal">&nbsp;&nbsp;/&nbsp;&nbsp;</span></command-palette-token>
              <command-palette-token data-text="projects_5" data-id="R_kgDOJx1vmw" data-type="repository" data-value="projects_5" data-targets="command-palette-scope.tokens" class="color-fg-default text-semibold" style="white-space:nowrap;line-height:20px;" id="" data-catalyst="">projects_5<span class="color-fg-subtle text-normal">&nbsp;&nbsp;/&nbsp;&nbsp;</span></command-palette-token>
        </command-palette-scope>
        <div class="command-palette-input-group flex-1 form-control border-0 box-shadow-none" style="z-index: 0">
          <div class="command-palette-typeahead position-absolute d-flex flex-items-center Truncate">
            <span class="typeahead-segment input-mirror" data-target="command-palette-input.mirror"></span>
            <span class="Truncate-text" data-target="command-palette-input.typeaheadText"></span>
            <span class="typeahead-segment" data-target="command-palette-input.typeaheadPlaceholder"></span>
          </div>
          <input class="js-overlay-input typeahead-input d-none" disabled="" tabindex="-1" aria-label="Hidden input for typeahead">
          <input type="text" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" class="js-input typeahead-input form-control border-0 box-shadow-none input-block width-full no-focus-indicator" aria-label="Command palette input" aria-haspopup="listbox" aria-expanded="false" aria-autocomplete="list" aria-controls="command-palette-page-stack" role="combobox" data-action="
              input:command-palette-input#onInput
              keydown:command-palette-input#onKeydown
            " placeholder="Search or jump to...">
        </div>
          <div data-view-component="true" class="position-relative d-inline-block">
    <button aria-keyshortcuts="Control+Backspace" data-action="click:command-palette-input#onClear keypress:command-palette-input#onClear" data-target="command-palette-input.clearButton" id="command-palette-clear-button" hidden="hidden" type="button" data-view-component="true" class="btn-octicon command-palette-input-clear-button" aria-labelledby="tooltip-156a0972-2023-40d3-b18d-bf0e60b53a5e">      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>    <tool-tip id="tooltip-156a0972-2023-40d3-b18d-bf0e60b53a5e" for="command-palette-clear-button" data-direction="w" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        position: absolute;
        z-index: 1000000;
        padding: .5em .75em;
        font: normal normal 11px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
        -webkit-font-smoothing: subpixel-antialiased;
        color: var(--color-fg-on-emphasis);
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--color-neutral-emphasis-plus);
        border-radius: 6px;
        opacity: 0;
        max-width: 250px;
        word-wrap: break-word;
        white-space: normal;
        width: max-content;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--color-neutral-emphasis-plus);
        content: "";
        border: 6px solid transparent;
        opacity: 0
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0
        }
        to {
          opacity: 1
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: ""
      }

      :host(.tooltip-open),
      :host(.tooltip-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--color-neutral-emphasis-plus)
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--color-neutral-emphasis-plus)
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%
      }

      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }

      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }

      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--color-neutral-emphasis-plus)
      }

      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--color-neutral-emphasis-plus)
      }
    </style><slot></slot></template>Clear Command Palette</tool-tip>
</div>
      </command-palette-input>

      <command-palette-page-stack data-default-scope-id="R_kgDOJx1vmw" data-default-scope-type="Repository" data-action="command-palette-page-octicons-cached:command-palette-page-stack#cacheOcticons" data-current-mode="" data-catalyst="" data-target="command-palette.pageStack" data-current-query-text="">
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search pull requests
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search issues
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search discussions
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">!</kbd> to search projects
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;owner&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">@</kbd> to search teams
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">@</kbd> to search people and organizations
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">&gt;</kbd> to activate command mode
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Go to your accessibility settings to change your keyboard shortcuts
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type author:@me to search your content
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:pr to filter to pull requests
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:issue to filter to issues
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:project to filter to projects
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:open to filter to open content
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
        <command-palette-tip class="mx-3 my-2 flash flash-error d-flex flex-items-center" data-scope-types="*" data-on-error="" data-mode="*" data-catalyst="" hidden="" data-match-mode="" data-value="*">
          <div>
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
          </div>
          <div class="px-2">
            We’ve encountered an error and some results aren't available at this time. Type a new search or try again later.
          </div>
        </command-palette-tip>
        <command-palette-tip class="h4 color-fg-default pl-3 pb-2 pt-3" data-on-empty="" data-scope-types="*" data-match-mode="[^?]|^$" data-mode="*" data-catalyst="" hidden="" data-value="*">
          No results matched your search
        </command-palette-tip>

        <div hidden="">

            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="arrow-right-color-fg-muted">
              <svg height="16" class="octicon octicon-arrow-right color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8.22 2.97a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l2.97-2.97H3.75a.75.75 0 0 1 0-1.5h7.44L8.22 4.03a.75.75 0 0 1 0-1.06Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="arrow-right-color-fg-default">
              <svg height="16" class="octicon octicon-arrow-right color-fg-default" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8.22 2.97a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l2.97-2.97H3.75a.75.75 0 0 1 0-1.5h7.44L8.22 4.03a.75.75 0 0 1 0-1.06Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="codespaces-color-fg-muted">
              <svg height="16" class="octicon octicon-codespaces color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="copy-color-fg-muted">
              <svg height="16" class="octicon octicon-copy color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="dash-color-fg-muted">
              <svg height="16" class="octicon octicon-dash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M2 7.75A.75.75 0 0 1 2.75 7h10a.75.75 0 0 1 0 1.5h-10A.75.75 0 0 1 2 7.75Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="file-color-fg-muted">
              <svg height="16" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="gear-color-fg-muted">
              <svg height="16" class="octicon octicon-gear color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="lock-color-fg-muted">
              <svg height="16" class="octicon octicon-lock color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M4 4a4 4 0 0 1 8 0v2h.25c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 12.25 15h-8.5A1.75 1.75 0 0 1 2 13.25v-5.5C2 6.784 2.784 6 3.75 6H4Zm8.25 3.5h-8.5a.25.25 0 0 0-.25.25v5.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25ZM10.5 6V4a2.5 2.5 0 1 0-5 0v2Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="moon-color-fg-muted">
              <svg height="16" class="octicon octicon-moon color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M9.598 1.591a.749.749 0 0 1 .785-.175 7.001 7.001 0 1 1-8.967 8.967.75.75 0 0 1 .961-.96 5.5 5.5 0 0 0 7.046-7.046.75.75 0 0 1 .175-.786Zm1.616 1.945a7 7 0 0 1-7.678 7.678 5.499 5.499 0 1 0 7.678-7.678Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="person-color-fg-muted">
              <svg height="16" class="octicon octicon-person color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6.004 6.004 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0ZM10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="pencil-color-fg-muted">
              <svg height="16" class="octicon octicon-pencil color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="issue-opened-open">
              <svg height="16" class="octicon octicon-issue-opened open" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="git-pull-request-draft-color-fg-muted">
              <svg height="16" class="octicon octicon-git-pull-request-draft color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M3.25 1A2.25 2.25 0 0 1 4 5.372v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.251 2.251 0 0 1 3.25 1Zm9.5 14a2.25 2.25 0 1 1 0-4.5 2.25 2.25 0 0 1 0 4.5ZM2.5 3.25a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0ZM3.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm9.5 0a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM14 7.5a1.25 1.25 0 1 1-2.5 0 1.25 1.25 0 0 1 2.5 0Zm0-4.25a1.25 1.25 0 1 1-2.5 0 1.25 1.25 0 0 1 2.5 0Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="search-color-fg-muted">
              <svg height="16" class="octicon octicon-search color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="sun-color-fg-muted">
              <svg height="16" class="octicon octicon-sun color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 12a4 4 0 1 1 0-8 4 4 0 0 1 0 8Zm0-1.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Zm5.657-8.157a.75.75 0 0 1 0 1.061l-1.061 1.06a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l1.06-1.06a.75.75 0 0 1 1.06 0Zm-9.193 9.193a.75.75 0 0 1 0 1.06l-1.06 1.061a.75.75 0 1 1-1.061-1.06l1.06-1.061a.75.75 0 0 1 1.061 0ZM8 0a.75.75 0 0 1 .75.75v1.5a.75.75 0 0 1-1.5 0V.75A.75.75 0 0 1 8 0ZM3 8a.75.75 0 0 1-.75.75H.75a.75.75 0 0 1 0-1.5h1.5A.75.75 0 0 1 3 8Zm13 0a.75.75 0 0 1-.75.75h-1.5a.75.75 0 0 1 0-1.5h1.5A.75.75 0 0 1 16 8Zm-8 5a.75.75 0 0 1 .75.75v1.5a.75.75 0 0 1-1.5 0v-1.5A.75.75 0 0 1 8 13Zm3.536-1.464a.75.75 0 0 1 1.06 0l1.061 1.06a.75.75 0 0 1-1.06 1.061l-1.061-1.06a.75.75 0 0 1 0-1.061ZM2.343 2.343a.75.75 0 0 1 1.061 0l1.06 1.061a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018l-1.06-1.06a.75.75 0 0 1 0-1.06Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="sync-color-fg-muted">
              <svg height="16" class="octicon octicon-sync color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M1.705 8.005a.75.75 0 0 1 .834.656 5.5 5.5 0 0 0 9.592 2.97l-1.204-1.204a.25.25 0 0 1 .177-.427h3.646a.25.25 0 0 1 .25.25v3.646a.25.25 0 0 1-.427.177l-1.38-1.38A7.002 7.002 0 0 1 1.05 8.84a.75.75 0 0 1 .656-.834ZM8 2.5a5.487 5.487 0 0 0-4.131 1.869l1.204 1.204A.25.25 0 0 1 4.896 6H1.25A.25.25 0 0 1 1 5.75V2.104a.25.25 0 0 1 .427-.177l1.38 1.38A7.002 7.002 0 0 1 14.95 7.16a.75.75 0 0 1-1.49.178A5.5 5.5 0 0 0 8 2.5Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="trash-color-fg-muted">
              <svg height="16" class="octicon octicon-trash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M11 1.75V3h2.25a.75.75 0 0 1 0 1.5H2.75a.75.75 0 0 1 0-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75ZM4.496 6.675l.66 6.6a.25.25 0 0 0 .249.225h5.19a.25.25 0 0 0 .249-.225l.66-6.6a.75.75 0 0 1 1.492.149l-.66 6.6A1.748 1.748 0 0 1 10.595 15h-5.19a1.75 1.75 0 0 1-1.741-1.575l-.66-6.6a.75.75 0 1 1 1.492-.15ZM6.5 1.75V3h3V1.75a.25.25 0 0 0-.25-.25h-2.5a.25.25 0 0 0-.25.25Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="key-color-fg-muted">
              <svg height="16" class="octicon octicon-key color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M10.5 0a5.499 5.499 0 1 1-1.288 10.848l-.932.932a.749.749 0 0 1-.53.22H7v.75a.749.749 0 0 1-.22.53l-.5.5a.749.749 0 0 1-.53.22H5v.75a.749.749 0 0 1-.22.53l-.5.5a.749.749 0 0 1-.53.22h-2A1.75 1.75 0 0 1 0 14.25v-2c0-.199.079-.389.22-.53l4.932-4.932A5.5 5.5 0 0 1 10.5 0Zm-4 5.5c-.001.431.069.86.205 1.269a.75.75 0 0 1-.181.768L1.5 12.56v1.69c0 .138.112.25.25.25h1.69l.06-.06v-1.19a.75.75 0 0 1 .75-.75h1.19l.06-.06v-1.19a.75.75 0 0 1 .75-.75h1.19l1.023-1.025a.75.75 0 0 1 .768-.18A4 4 0 1 0 6.5 5.5ZM11 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="comment-discussion-color-fg-muted">
              <svg height="16" class="octicon octicon-comment-discussion color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="bell-color-fg-muted">
              <svg height="16" class="octicon octicon-bell color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 16a2 2 0 0 0 1.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 0 0 8 16ZM3 5a5 5 0 0 1 10 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.519 1.519 0 0 1 13.482 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947Zm5-3.5A3.5 3.5 0 0 0 4.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01l.001.006c0 .002.002.004.004.006l.006.004.007.001h10.964l.007-.001.006-.004.004-.006.001-.007a.017.017 0 0 0-.003-.01l-1.703-2.554a1.745 1.745 0 0 1-.294-.97V5A3.5 3.5 0 0 0 8 1.5Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="bell-slash-color-fg-muted">
              <svg height="16" class="octicon octicon-bell-slash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="m4.182 4.31.016.011 10.104 7.316.013.01 1.375.996a.75.75 0 1 1-.88 1.214L13.626 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947V5.305L.31 3.357a.75.75 0 1 1 .88-1.214Zm7.373 7.19L4.5 6.391v1.556c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01c0 .005.002.009.005.012l.006.004.007.001ZM8 1.5c-.997 0-1.895.416-2.534 1.086A.75.75 0 1 1 4.38 1.55 5 5 0 0 1 13 5v2.373a.75.75 0 0 1-1.5 0V5A3.5 3.5 0 0 0 8 1.5ZM8 16a2 2 0 0 1-1.985-1.75c-.017-.137.097-.25.235-.25h3.5c.138 0 .252.113.235.25A2 2 0 0 1 8 16Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="paintbrush-color-fg-muted">
              <svg height="16" class="octicon octicon-paintbrush color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M11.134 1.535c.7-.509 1.416-.942 2.076-1.155.649-.21 1.463-.267 2.069.34.603.601.568 1.411.368 2.07-.202.668-.624 1.39-1.125 2.096-1.011 1.424-2.496 2.987-3.775 4.249-1.098 1.084-2.132 1.839-3.04 2.3a3.744 3.744 0 0 1-1.055 3.217c-.431.431-1.065.691-1.657.861-.614.177-1.294.287-1.914.357A21.151 21.151 0 0 1 .797 16H.743l.007-.75H.749L.742 16a.75.75 0 0 1-.743-.742l.743-.008-.742.007v-.054a21.25 21.25 0 0 1 .13-2.284c.067-.647.187-1.287.358-1.914.17-.591.43-1.226.86-1.657a3.746 3.746 0 0 1 3.227-1.054c.466-.893 1.225-1.907 2.314-2.982 1.271-1.255 2.833-2.75 4.245-3.777ZM1.62 13.089c-.051.464-.086.929-.104 1.395.466-.018.932-.053 1.396-.104a10.511 10.511 0 0 0 1.668-.309c.526-.151.856-.325 1.011-.48a2.25 2.25 0 1 0-3.182-3.182c-.155.155-.329.485-.48 1.01a10.515 10.515 0 0 0-.309 1.67Zm10.396-10.34c-1.224.89-2.605 2.189-3.822 3.384l1.718 1.718c1.21-1.205 2.51-2.597 3.387-3.833.47-.662.78-1.227.912-1.662.134-.444.032-.551.009-.575h-.001V1.78c-.014-.014-.113-.113-.548.027-.432.14-.995.462-1.655.942Zm-4.832 7.266-.001.001a9.859 9.859 0 0 0 1.63-1.142L7.155 7.216a9.7 9.7 0 0 0-1.161 1.607c.482.302.889.71 1.19 1.192Z"></path></svg>
            </div>

            <command-palette-item-group data-group-id="top" data-group-title="Top result" data-group-hint="" data-group-limits="{}" data-default-priority="0" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Top result
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Top result results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="commands" data-group-title="Commands" data-group-hint="Type &gt; to filter" data-group-limits="{&quot;static_items_page&quot;:50,&quot;issue&quot;:50,&quot;pull_request&quot;:50,&quot;discussion&quot;:50}" data-default-priority="1" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Commands
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              Type &gt; to filter
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Commands results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="global_commands" data-group-title="Global Commands" data-group-hint="Type &gt; to filter" data-group-limits="{&quot;issue&quot;:0,&quot;pull_request&quot;:0,&quot;discussion&quot;:0}" data-default-priority="2" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Global Commands
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              Type &gt; to filter
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Global Commands results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="this_page" data-group-title="This Page" data-group-hint="" data-group-limits="{}" data-default-priority="3" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              This Page
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="This Page results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="files" data-group-title="Files" data-group-hint="" data-group-limits="{}" data-default-priority="4" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Files
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Files results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="default" data-group-title="Default" data-group-hint="" data-group-limits="{&quot;static_items_page&quot;:50}" data-default-priority="5" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Default results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="pages" data-group-title="Pages" data-group-hint="" data-group-limits="{&quot;repository&quot;:10}" data-default-priority="6" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Pages
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Pages results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="access_policies" data-group-title="Access Policies" data-group-hint="" data-group-limits="{}" data-default-priority="7" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Access Policies
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Access Policies results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="organizations" data-group-title="Organizations" data-group-hint="" data-group-limits="{}" data-default-priority="8" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Organizations
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Organizations results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="repositories" data-group-title="Repositories" data-group-hint="" data-group-limits="{}" data-default-priority="9" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Repositories
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Repositories results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="references" data-group-title="Issues, pull requests, and discussions" data-group-hint="Type # to filter" data-group-limits="{}" data-default-priority="10" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Issues, pull requests, and discussions
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              Type # to filter
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Issues, pull requests, and discussions results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="teams" data-group-title="Teams" data-group-hint="" data-group-limits="{}" data-default-priority="11" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Teams
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Teams results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="users" data-group-title="Users" data-group-hint="" data-group-limits="{}" data-default-priority="12" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Users
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Users results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="memex_projects" data-group-title="Projects" data-group-hint="" data-group-limits="{}" data-default-priority="13" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Projects
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Projects results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="projects" data-group-title="Projects (classic)" data-group-hint="" data-group-limits="{}" data-default-priority="14" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Projects (classic)
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Projects (classic) results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="footer" data-group-title="Footer" data-group-hint="" data-group-limits="{}" data-default-priority="15" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Footer results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="modes_help" data-group-title="Modes" data-group-hint="" data-group-limits="{}" data-default-priority="16" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Modes
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Modes results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="filters_help" data-group-title="Use filters in issues, pull requests, discussions, and projects" data-group-hint="" data-group-limits="{}" data-default-priority="17" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Use filters in issues, pull requests, discussions, and projects
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Use filters in issues, pull requests, discussions, and projects results"></div>
        </command-palette-item-group>

            <command-palette-page data-page-title="PowerstarPrasad" data-scope-id="U_kgDOCC1RSg" data-scope-type="owner" data-targets="command-palette-page-stack.defaultPages" hidden="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" style="max-height:400px;">
            </command-palette-page>
            <command-palette-page data-page-title="projects_5" data-scope-id="R_kgDOJx1vmw" data-scope-type="repository" data-targets="command-palette-page-stack.defaultPages" hidden="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" style="max-height:400px;">
            </command-palette-page>
        </div>

        <command-palette-page data-is-root="" hidden="" data-page-title="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" data-targets="command-palette-page-stack.pages" style="max-height:400px;" data-scope-id="" data-scope-type="">
        </command-palette-page>
          <command-palette-page data-page-title="PowerstarPrasad" data-scope-id="U_kgDOCC1RSg" data-scope-type="owner" hidden="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" data-targets="command-palette-page-stack.pages" style="max-height:400px;">
          </command-palette-page>
          <command-palette-page data-page-title="projects_5" data-scope-id="R_kgDOJx1vmw" data-scope-type="repository" hidden="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" data-targets="command-palette-page-stack.pages" style="max-height:400px;">
          </command-palette-page>
      </command-palette-page-stack>

      <server-defined-provider data-type="search-links" data-targets="command-palette.serverDefinedProviderElements" data-supported-modes="" data-catalyst="" data-fetch-debounce="" data-supported-scope-types="" data-src="" data-supports-commands=""></server-defined-provider>
      <server-defined-provider data-type="help" data-targets="command-palette.serverDefinedProviderElements" data-supported-modes="" data-catalyst="" data-fetch-debounce="" data-supported-scope-types="" data-src="" data-supports-commands="">
          <command-palette-help data-group="modes_help" data-prefix="#" data-scope-types="[&quot;&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>issues</strong> and <strong>pull requests</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">#</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="#" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>issues, pull requests, discussions,</strong> and <strong>projects</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">#</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="@" data-scope-types="[&quot;&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>organizations, repositories,</strong> and <strong>users</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">@</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="!" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>projects</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">!</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="/" data-scope-types="[&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>files</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">/</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="&gt;" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Activate <strong>command mode</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">&gt;</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# author:@me" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search your issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># author:@me</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# author:@me" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search your issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># author:@me</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:pr" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to pull requests</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:pr</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:issue" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to issues</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:issue</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:discussion" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:discussion</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:project" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to projects</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:project</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:open" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to open issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:open</kbd>
              </span>
          </command-palette-help>
      </server-defined-provider>

        <server-defined-provider data-type="commands" data-fetch-debounce="0" data-src="/command_palette/commands" data-supported-modes="[]" data-supports-commands="" data-targets="command-palette.serverDefinedProviderElements" data-supported-scope-types="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="prefetched" data-fetch-debounce="0" data-src="/command_palette/jump_to_page_navigation" data-supported-modes="[&quot;&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/issues" data-supported-modes="[&quot;#&quot;,&quot;#&quot;]" data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;,&quot;&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/jump_to" data-supported-modes="[&quot;@&quot;,&quot;@&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/jump_to_members_only" data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="prefetched" data-fetch-debounce="0" data-src="/command_palette/jump_to_members_only_prefetched" data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="files" data-fetch-debounce="0" data-src="/command_palette/files" data-supported-modes="[&quot;/&quot;]" data-supported-scope-types="[&quot;repository&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/discussions" data-supported-modes="[&quot;#&quot;]" data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/projects" data-supported-modes="[&quot;#&quot;,&quot;!&quot;]" data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="prefetched" data-fetch-debounce="0" data-src="/command_palette/recent_issues" data-supported-modes="[&quot;#&quot;,&quot;#&quot;]" data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;,&quot;&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/teams" data-supported-modes="[&quot;@&quot;,&quot;&quot;]" data-supported-scope-types="[&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/name_with_owner_repository" data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
    <client-defined-provider data-catalyst="" data-provider-id="main-window-commands-provider" data-targets="command-palette.clientDefinedProviderElements"></client-defined-provider></command-palette>
  </details-dialog>
</details>

<div class="position-fixed bottom-0 left-0 ml-5 mb-5 js-command-palette-toasts" style="z-index: 1000">
  <div hidden="" class="Toast Toast--loading">
    <span class="Toast-icon">
      <svg class="Toast--spinner" viewBox="0 0 32 32" width="18" height="18" aria-hidden="true">
        <path fill="#959da5" d="M16 0 A16 16 0 0 0 16 32 A16 16 0 0 0 16 0 M16 4 A12 12 0 0 1 16 28 A12 12 0 0 1 16 4"></path>
        <path fill="#ffffff" d="M16 0 A16 16 0 0 1 32 16 L28 16 A12 12 0 0 0 16 4z"></path>
      </svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden="" class="anim-fade-in fast Toast Toast--error">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden="" class="anim-fade-in fast Toast Toast--warning">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>


  <div hidden="" class="anim-fade-in fast Toast Toast--success">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden="" class="anim-fade-in fast Toast">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-info">
    <path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8Zm8-6.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13ZM6.5 7.75A.75.75 0 0 1 7.25 7h1a.75.75 0 0 1 .75.75v2.75h.25a.75.75 0 0 1 0 1.5h-2a.75.75 0 0 1 0-1.5h.25v-2h-.25a.75.75 0 0 1-.75-.75ZM8 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>
</div>


  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container">
      
      






    
  <div id="repository-container-header" data-turbo-replace="" hidden=""></div>




<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content ">
      <a href="https://github.dev/" class="d-none js-github-dev-shortcut" data-hotkey=".">Open in github.dev</a>
  <a href="https://github.dev/" class="d-none js-github-dev-new-tab-shortcut" data-hotkey="Shift+.,Shift+&gt;,&gt;" target="_blank">Open in a new github.dev tab</a>
    <a class="d-none" data-hotkey="," target="_blank" href="https://github.com/codespaces/new/PowerstarPrasad/projects_5/tree/main?resume=1">Open in codespace</a>



    
      
    





<react-app app-name="react-code-view" initial-path="/PowerstarPrasad/projects_5/blob/main/railway%20project.py" style="min-height: calc(100vh - 62px)" data-ssr="false" data-lazy="false" data-alternate="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"allShortcutsEnabled":true,"fileTree":{"":{"items":[{"name":"LordTiru_Bank-Project.py","path":"LordTiru_Bank-Project.py","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"railway project.py","path":"railway project.py","contentType":"file"},{"name":"super-market project.py","path":"super-market project.py","contentType":"file"},{"name":"titanic_project.ipynb","path":"titanic_project.ipynb","contentType":"file"}],"totalCount":5}},"fileTreeProcessingTime":2.525262,"foldersToFetch":[],"reducedMotionEnabled":"system","repo":{"id":656240539,"defaultBranch":"main","name":"projects_5","ownerLogin":"PowerstarPrasad","currentUserCanPush":true,"isFork":true,"isEmpty":false,"createdAt":"2023-06-20T20:04:38.000+05:30","ownerAvatar":"https://avatars.githubusercontent.com/u/137187658?v=4","public":true,"private":false,"isOrgOwned":false},"refInfo":{"name":"main","listCacheKey":"v0:1687271806.5804448","canEdit":true,"refType":"branch","currentOid":"deae9d422fd0dc3289025b3b80f8a51727124733"},"path":"railway project.py","currentUser":{"id":137187658,"login":"PowerstarPrasad","userEmail":"ugangaprasad33@gmail.com"},"blob":{"rawBlob":"import random\r\nimport pickle\r\nimport sys\r\n\r\nlogged_in = False\r\nuid = 0\r\npwd = ''\r\n\r\nclass train:\r\n    def __init__(self,name = '', num = 0, arr_time = '',dep_time = '',src = '' ,des = '',day_of_travel = '',seat_available_in_1AC = 0,seat_available_in_2AC = 0,seat_available_in_SL = 0,fare_1ac = 0, fare_2ac = 0 ,fare_sl = 0):\r\n        self.name = name\r\n        self.num = num\r\n        self.arr_time = arr_time\r\n        self.dep_time = dep_time\r\n        self.src = src\r\n        self.des = des\r\n        self.day_of_travel = day_of_travel\r\n        self.seats = {'1AC' : seat_available_in_1AC, '2AC': seat_available_in_2AC,'SL': seat_available_in_SL}\r\n        self.fare = {'1AC' : fare_1ac,'2AC' : fare_2ac ,'SL' : fare_sl}\r\n    def print_seat_availablity(self):\r\n    \tprint(\"No. of seats available in 1AC :- \"+str(self.seats['1AC']))\r\n    \tprint(\"No. of seats available in 2AC :- \"+str(self.seats['2AC']))\r\n    \tprint(\"No. of seats available in SL :- \"+str(self.seats['SL']))\r\n    def check_availabilty(self,coach='',ticket_num = 0):\r\n    \tcoach = coach.upper()\r\n    \tif coach not in ('SL','1AC','2AC'):\r\n    \t\tprint_seat_availablity()\r\n    \t\tcoach = input(\"Enter the coach(1AC/2AC/SL) :-\")\r\n    \telse:\r\n    \t\tif self.seats[coach] == 0:\r\n    \t\t\treturn False\r\n    \t\telif self.seats[coach] \u003e= ticket_num:\r\n    \t\t\treturn True\r\n    \t\telse:\r\n    \t\t\treturn False\r\n    def book_ticket(self,coach = '',no_of_tickets = 0):\r\n    \tself.seats[coach] -= no_of_tickets\r\n    \treturn True\r\n\r\n\r\nclass ticket:\r\n\tdef __init__(self,train,user,ticket_num,coach):\r\n\t\tself.pnr = str(train.num)+str(user.uid)+str(random.randint(100,999))\r\n\t\tself.train_num = train.num\r\n\t\tself.coach = coach\r\n\t\tself.uid = user.uid\r\n\t\tself.train_name = train.name\r\n\t\tself.user_name = user.name\r\n\t\tself.ticket_num = ticket_num\r\n\t\tuser.history.update({self.pnr : self})\r\n\t\tticket_dict.update({self.pnr : self})\r\n\r\n\r\n\r\nclass user:\r\n\tdef __init__(self,uid = 0,name = '',hometown = '',cell_num = '',pwd = ''):\r\n\t\tself.uid = uid\r\n\t\tself.name = name\r\n\t\tself.hometown = ''\r\n\t\tself.cell_num = ''\r\n\t\tself.pwd = pwd\r\n\t\tself.history = {}\r\n\r\n\r\nclass acceptors:\r\n\t''' Class containing functions for accepting and \r\n\tvalidating values properly'''\r\n\tdef accept_uid():\r\n\t\tuid = 0\r\n\t\ttry:\r\n\t\t\tuid = int(input(\"Enter the User ID:- \"))\r\n\t\texcept ValueError:\r\n\t\t\tprint(\"Please enter user ID properly.\")\r\n\t\t\treturn acceptors.accept_uid()\r\n\t\telse:\r\n\t\t\treturn uid\r\n\r\n\tdef accept_pwd():\r\n\t\tpwd = input(\"Enter your password:- \")\r\n\t\treturn pwd\r\n\r\n\r\n\tdef accept_train_number():\r\n\t\ttrain_num = 0\r\n\t\ttry:\r\n\t\t\ttrain_num = int(input(\"Enter the train number :- \"))\r\n\t\texcept ValueError:\r\n\t\t\tprint(\"Please enter train number properly.\")\r\n\t\t\treturn acceptors.accept_train_number()\r\n\t\telse:\r\n\t\t\tif train_num not in trains:\r\n\t\t\t\tprint(\"Please enter a valid train number.\")\r\n\t\t\t\treturn acceptors.accept_train_number()\r\n\t\t\telse:\r\n\t\t\t\treturn train_num\r\n\t\r\n\r\n\r\n\tdef accept_menu_option():\r\n\t\toption = input(\"Enter your option :- \")\r\n\t\tif option not in ('1','2','3','4','5','6','7','8'):\r\n\t\t\tprint(\"Please enter a valid option!\")\r\n\t\t\treturn acceptors.accept_menu_option()\r\n\t\telse:\r\n\t\t\treturn int(option)\r\n\r\n\tdef accept_coach():\r\n\t\tcoach = input(\"Enter the coach :- \")\r\n\t\tcoach = coach.upper()\r\n\t\tif coach not in ('SL','1AC','2AC'):\r\n\t\t\tprint(\"Please enter coach properly.\")\r\n\t\t\treturn acceptors.accept_coach()\r\n\t\telse:\r\n\t\t\treturn coach\r\n\r\n\tdef accept_prompt():\r\n\t\tprompt = input(\"Confirm? (y/n) :-\")\r\n\t\tif prompt not in ('y','n'):\r\n\t\t\tprint(\"Please enter proper choice.\")\r\n\t\t\treturn acceptors.accept_prompt()\r\n\t\treturn prompt\t\t\r\n\r\n\tdef accept_ticket_num():\r\n\t\tticket_num = 0\r\n\t\ttry:\r\n\t\t\tticket_num = int(input(\"Enter the number of tickets :- \"))\r\n\t\t\tif ticket_num \u003c 0:\r\n\t\t\t\traise ValueError\r\n\t\texcept ValueError:\r\n\t\t\tprint(\"Enter proper ticket number.\")\r\n\t\t\treturn acceptors.accept_ticket_num()\r\n\t\telse:\r\n\t\t\treturn ticket_num\r\n\tdef accept_pnr():\r\n\t\tpnr = input(\"Enter your PNR number :- \")\r\n\t\tif pnr not in ticket_dict:\r\n\t\t\tprint(\"Please enter proper PNR number :- \")\r\n\t\t\treturn acceptors.accept_pnr()\r\n\t\telse:\r\n\t\t\treturn pnr\r\n\r\n\r\n\r\ndef book_ticket():\r\n\tif not logged_in:\r\n\t\tlogin('p')\r\n\r\n\tcheck_seat_availabilty('p')\r\n\tchoice = acceptors.accept_train_number()\r\n\ttrains[choice].print_seat_availablity()\r\n\tcoach = acceptors.accept_coach()\r\n\tticket_num = acceptors.accept_ticket_num()\r\n\tif trains[choice].check_availabilty(coach,ticket_num):\r\n\t\tprint(\"You have to pay :- \",trains[choice].fare[coach]*ticket_num,\"  \")\r\n\t\tprompt = acceptors.accept_prompt()\r\n\t\tif prompt == 'y':\r\n\t\t\ttrains[choice].book_ticket(coach,ticket_num)\r\n\t\t\tprint(\"Booking Successful!\\n\\n\")\r\n\t\t\ttick = ticket(trains[choice],users[uid],ticket_num,coach)\r\n\t\t\tprint(\"Please note PNR number :- \",tick.pnr,\"\\n\\n\")\r\n\t\t\tmenu()\r\n\t\telse:\r\n\t\t\tprint(\"Exiting...\\n\\n\")\r\n\t\t\tmenu()\r\n\telse:\r\n\t\tprint(ticket_num,\" tickets not available\")\r\n\t\tmenu()\r\n\r\ndef cancel_ticket():\r\n\tpnr = acceptors.accept_pnr()\r\n\tif pnr in ticket_dict:\r\n\t\tcheck_pnr(pnr)\r\n\t\tprint(\"Cancel the tickets?\")\r\n\t\tprompt = acceptors.accept_prompt()\r\n\t\tif prompt == 'y':\r\n\t\t\tif logged_in:\r\n\t\t\t\tprint(\"Ticket Cancelled.\\n\")\r\n\t\t\t\ttrains[ticket_dict[pnr].train_num].seats[ticket_dict[pnr].coach] += ticket_dict[pnr].ticket_num\r\n\t\t\t\tdel users[ticket_dict[pnr].uid].history[pnr]\r\n\t\t\t\tdel ticket_dict[pnr]\r\n\t\t\telse:\r\n\t\t\t\tlogin('p')\r\n\t\t\t\tprint(\"Ticket Cancelled.\\n\")\r\n\t\t\t\ttrains[ticket_dict[pnr].train_num].seats[ticket_dict[pnr].coach] += ticket_dict[pnr].ticket_num\r\n\t\t\t\tdel users[ticket_dict[pnr].uid].history[pnr]\r\n\t\t\t\tdel ticket_dict[pnr]\r\n\t\telse:\r\n\t\t\tprint(\"\\nTicket not cancelled\\n\")\r\n\tmenu()\r\n\r\n\r\n\r\ndef check_seat_availabilty(flag = ''):\r\n\tsrc = input(\"Enter the source station:- \")\r\n\tdes = input(\"Enter the destination station:- \")\r\n\tflag_2 = 0\r\n\tfor i in trains:\r\n\t\tif trains[i].src == src and trains[i].des == des:\r\n\t\t\tprint(\"Train Name :- \",trains[i].name ,\" \" ,\"Number \",trains[i].num ,\" \",\"Day of Travel :- \",trains[i].day_of_travel)\r\n\t\t\tflag_2 += 1\r\n\tif flag_2 == 0:\r\n\t\tprint(\"\\nNo trains found between the stations you entered.\\n\")\r\n\t\tmenu()\r\n\tif flag == '':\r\n\t\ttrain_num = acceptors.accept_train_number()\r\n\t\ttrains[train_num].print_seat_availablity()\r\n\t\tmenu()\r\n\telse:\r\n\t\tpass\r\n\r\ndef check_pnr(pnr = ''):\r\n\tif pnr == '':\r\n\t\tpnr = acceptors.accept_pnr()\r\n\t\tprint()\r\n\t\tprint(\"User name:- \",ticket_dict[pnr].user_name)\r\n\t\tprint(\"Train name:- \",ticket_dict[pnr].train_name)\r\n\t\tprint(\"Train number:- \",ticket_dict[pnr].train_num,\" Source:- \",trains[ticket_dict[pnr].train_num].src,\" Destination:- \",trains[ticket_dict[pnr].train_num].des)\r\n\t\tprint(\"No. of Tickets Booked :- \",ticket_dict[pnr].ticket_num)\r\n\t\tprint()\r\n\t\tmenu()\r\n\telse:\r\n\t\tprint()\r\n\t\tprint(\"User name:- \",ticket_dict[pnr].user_name)\r\n\t\tprint(\"Train name:- \",ticket_dict[pnr].train_name)\r\n\t\tprint(\"Train number:- \",ticket_dict[pnr].train_num,\" Source:- \",trains[ticket_dict[pnr].train_num].src,\" Destination:- \",trains[ticket_dict[pnr].train_num].des)\r\n\t\tprint(\"No. of Tickets Booked :- \",ticket_dict[pnr].ticket_num)\r\n\t\tprint()\r\n\r\ndef create_new_acc():\r\n\tuser_name = input(\"Enter your user name:- \")\r\n\tpwd = input(\"Enter your password :- \")\r\n\tuid = random.randint(1000,9999)\r\n\thometown = input(\"Enter your hometown :- \")\r\n\tcell_num = input(\"Enter your phone number :- \")\r\n\tu = user(uid, user_name, hometown, cell_num, pwd)\r\n\tprint(\"Your user ID is :- \",uid)\r\n\tusers.update({u.uid : u})\r\n\tmenu()\r\n\r\n\r\n\r\ndef login(flag = ''):\r\n\tglobal uid\r\n\tglobal pwd\r\n\tuid = acceptors.accept_uid()\r\n\tpwd = acceptors.accept_pwd()\r\n\tif uid in users and users[uid].pwd == pwd:\t\t\r\n\t\tprint(\"\\nWelcome \",users[uid].name,\" !\\n\")\r\n\t\tglobal logged_in\r\n\t\tlogged_in = True\r\n\telse:\r\n\t\tprint(\"\\nNo such user ID / Wrong Password !\\n\")\r\n\t\treturn login()\r\n\tif flag == '':\r\n\t\tmenu()\r\n\telse:\r\n\t\tpass\r\n\r\ndef check_prev_bookings():\r\n\tif not logged_in:\r\n\t\tlogin('p')\r\n\tfor i in users[uid].history:\r\n\t\tprint(\"\\nPNR number = \",i)\r\n\t\tcheck_pnr(i)\r\n\tmenu()\r\n\r\ndef end():\r\n\ts()\r\n\tprint(\"------------------------------------------------Thank You!-----------------------------------------------------------------------\")\r\n\tprint(\"---------------------------------------------------------------------------------------------------------------------------------\")\r\n\tsys.exit()\r\n\r\n\r\nt1 = train('Bokara Express',12345,'12:34','22:12','vsk','vij','Wed',30,23,43,2205,320,234)\r\nt2 = train('gunupur',12565,'02:34','23:12','che','kol','Mon',33,4,12,3434,435,234)\r\nt3 = train('Vandey Bharat',22353,'11:56','03:12','hyb','vsk','Fri',33,24,77,455,325,533)\r\ntrains = {t1.num:t1,t2.num:t2,t3.num:t3}\r\nu1 = user(1212,'venky','rajahmundry','903802','venky')\r\nu2 = user(2322,'gvl dash','dash','945210','gvldash')\r\nusers={u1.uid : u1, u2.uid : u2}\r\nticket_dict = {}\r\n\r\ndef load():\r\n\tglobal  trains,users,ticket_dict\r\n\twith open(\"data.pkl\",\"rb\") as f:\r\n\t\ttrains = pickle.load(f)\r\n\t\tusers = pickle.load(f)\r\n\t\tticket_dict = pickle.load(f)\r\n\r\n\r\n\r\ndef s():\r\n\twith open(\"data.pkl\",\"wb\") as f:\r\n\t\tpickle.dump(trains,f)\r\n\t\tpickle.dump(users,f)\r\n\t\tpickle.dump(ticket_dict,f)\r\n\r\n\r\n\r\nprint(\"\\n\")\r\nprint(\"     \u003e\u003e\u003e\u003e\u003e-----------\u003e\u003e    Welcome to Railway Reservation Portal     \u003c\u003c----------\u003c\u003c\u003c\u003c\u003c  \")\r\nprint(\"--\"*50)\r\n# load()\r\n\r\n\r\ndef menu():\r\n\tprint(\"Choose one of the following option:-\")\r\n\tprint(\"1.Book Ticket\")\r\n\tprint(\"2.Cancel Ticket\")\r\n\tprint(\"3.Check PNR \")\r\n\tprint(\"4.Check seat availibity\")\r\n\tprint(\"5.Create new account\")\r\n\tprint(\"6.Check previous bookings\")\r\n\tprint(\"7.Login\")\r\n\tprint(\"8.Exit\")\r\n\tfunc = { 1 : book_ticket, 2 : cancel_ticket, 3 : check_pnr, 4 : check_seat_availabilty, 5 : create_new_acc, 6 : check_prev_bookings, 7 : login, 8 : end}\r\n\toption = acceptors.accept_menu_option()\r\n\tfunc[option]()\r\n\t\r\n\r\nmenu()\r\n\r\n","colorizedLines":null,"stylingDirectives":[[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":13,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":13,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-s1"}],[],[{"start":0,"end":9,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":17,"cssClass":"pl-c1"}],[{"start":0,"end":3,"cssClass":"pl-s1"},{"start":4,"end":5,"cssClass":"pl-c1"},{"start":6,"end":7,"cssClass":"pl-c1"}],[{"start":0,"end":3,"cssClass":"pl-s1"},{"start":4,"end":5,"cssClass":"pl-c1"},{"start":6,"end":8,"cssClass":"pl-s"}],[],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":11,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":16,"cssClass":"pl-en"},{"start":17,"end":21,"cssClass":"pl-s1"},{"start":22,"end":26,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":29,"end":31,"cssClass":"pl-s"},{"start":33,"end":36,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-c1"},{"start":39,"end":40,"cssClass":"pl-c1"},{"start":42,"end":50,"cssClass":"pl-s1"},{"start":51,"end":52,"cssClass":"pl-c1"},{"start":53,"end":55,"cssClass":"pl-s"},{"start":56,"end":64,"cssClass":"pl-s1"},{"start":65,"end":66,"cssClass":"pl-c1"},{"start":67,"end":69,"cssClass":"pl-s"},{"start":70,"end":73,"cssClass":"pl-s1"},{"start":74,"end":75,"cssClass":"pl-c1"},{"start":76,"end":78,"cssClass":"pl-s"},{"start":80,"end":83,"cssClass":"pl-s1"},{"start":84,"end":85,"cssClass":"pl-c1"},{"start":86,"end":88,"cssClass":"pl-s"},{"start":89,"end":102,"cssClass":"pl-s1"},{"start":103,"end":104,"cssClass":"pl-c1"},{"start":105,"end":107,"cssClass":"pl-s"},{"start":108,"end":129,"cssClass":"pl-s1"},{"start":130,"end":131,"cssClass":"pl-c1"},{"start":132,"end":133,"cssClass":"pl-c1"},{"start":134,"end":155,"cssClass":"pl-s1"},{"start":156,"end":157,"cssClass":"pl-c1"},{"start":158,"end":159,"cssClass":"pl-c1"},{"start":160,"end":180,"cssClass":"pl-s1"},{"start":181,"end":182,"cssClass":"pl-c1"},{"start":183,"end":184,"cssClass":"pl-c1"},{"start":185,"end":193,"cssClass":"pl-s1"},{"start":194,"end":195,"cssClass":"pl-c1"},{"start":196,"end":197,"cssClass":"pl-c1"},{"start":199,"end":207,"cssClass":"pl-s1"},{"start":208,"end":209,"cssClass":"pl-c1"},{"start":210,"end":211,"cssClass":"pl-c1"},{"start":213,"end":220,"cssClass":"pl-s1"},{"start":221,"end":222,"cssClass":"pl-c1"},{"start":223,"end":224,"cssClass":"pl-c1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":24,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":22,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":32,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":32,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":22,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":22,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":26,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":29,"end":42,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":22,"end":27,"cssClass":"pl-s"},{"start":30,"end":51,"cssClass":"pl-s1"},{"start":53,"end":58,"cssClass":"pl-s"},{"start":60,"end":81,"cssClass":"pl-s1"},{"start":82,"end":86,"cssClass":"pl-s"},{"start":88,"end":108,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":21,"end":26,"cssClass":"pl-s"},{"start":29,"end":37,"cssClass":"pl-s1"},{"start":38,"end":43,"cssClass":"pl-s"},{"start":46,"end":54,"cssClass":"pl-s1"},{"start":56,"end":60,"cssClass":"pl-s"},{"start":63,"end":70,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":30,"cssClass":"pl-en"},{"start":31,"end":35,"cssClass":"pl-s1"}],[{"start":5,"end":10,"cssClass":"pl-en"},{"start":11,"end":46,"cssClass":"pl-s"},{"start":46,"end":47,"cssClass":"pl-c1"},{"start":47,"end":50,"cssClass":"pl-en"},{"start":51,"end":55,"cssClass":"pl-s1"},{"start":56,"end":61,"cssClass":"pl-s1"},{"start":62,"end":67,"cssClass":"pl-s"}],[{"start":5,"end":10,"cssClass":"pl-en"},{"start":11,"end":46,"cssClass":"pl-s"},{"start":46,"end":47,"cssClass":"pl-c1"},{"start":47,"end":50,"cssClass":"pl-en"},{"start":51,"end":55,"cssClass":"pl-s1"},{"start":56,"end":61,"cssClass":"pl-s1"},{"start":62,"end":67,"cssClass":"pl-s"}],[{"start":5,"end":10,"cssClass":"pl-en"},{"start":11,"end":45,"cssClass":"pl-s"},{"start":45,"end":46,"cssClass":"pl-c1"},{"start":46,"end":49,"cssClass":"pl-en"},{"start":50,"end":54,"cssClass":"pl-s1"},{"start":55,"end":60,"cssClass":"pl-s1"},{"start":61,"end":65,"cssClass":"pl-s"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":25,"cssClass":"pl-en"},{"start":26,"end":30,"cssClass":"pl-s1"},{"start":31,"end":36,"cssClass":"pl-s1"},{"start":36,"end":37,"cssClass":"pl-c1"},{"start":37,"end":39,"cssClass":"pl-s"},{"start":40,"end":50,"cssClass":"pl-s1"},{"start":51,"end":52,"cssClass":"pl-c1"},{"start":53,"end":54,"cssClass":"pl-c1"}],[{"start":5,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":18,"cssClass":"pl-s1"},{"start":19,"end":24,"cssClass":"pl-en"}],[{"start":5,"end":7,"cssClass":"pl-k"},{"start":8,"end":13,"cssClass":"pl-s1"},{"start":14,"end":17,"cssClass":"pl-c1"},{"start":18,"end":20,"cssClass":"pl-c1"},{"start":22,"end":26,"cssClass":"pl-s"},{"start":27,"end":32,"cssClass":"pl-s"},{"start":33,"end":38,"cssClass":"pl-s"}],[{"start":6,"end":28,"cssClass":"pl-en"}],[{"start":6,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":19,"cssClass":"pl-en"},{"start":20,"end":52,"cssClass":"pl-s"}],[{"start":5,"end":9,"cssClass":"pl-k"}],[{"start":6,"end":8,"cssClass":"pl-k"},{"start":9,"end":13,"cssClass":"pl-s1"},{"start":14,"end":19,"cssClass":"pl-s1"},{"start":20,"end":25,"cssClass":"pl-s1"},{"start":27,"end":29,"cssClass":"pl-c1"},{"start":30,"end":31,"cssClass":"pl-c1"}],[{"start":7,"end":13,"cssClass":"pl-k"},{"start":14,"end":19,"cssClass":"pl-c1"}],[{"start":6,"end":10,"cssClass":"pl-k"},{"start":11,"end":15,"cssClass":"pl-s1"},{"start":16,"end":21,"cssClass":"pl-s1"},{"start":22,"end":27,"cssClass":"pl-s1"},{"start":29,"end":31,"cssClass":"pl-c1"},{"start":32,"end":42,"cssClass":"pl-s1"}],[{"start":7,"end":13,"cssClass":"pl-k"},{"start":14,"end":18,"cssClass":"pl-c1"}],[{"start":6,"end":10,"cssClass":"pl-k"}],[{"start":7,"end":13,"cssClass":"pl-k"},{"start":14,"end":19,"cssClass":"pl-c1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":19,"cssClass":"pl-en"},{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":30,"cssClass":"pl-s1"},{"start":31,"end":32,"cssClass":"pl-c1"},{"start":33,"end":35,"cssClass":"pl-s"},{"start":36,"end":49,"cssClass":"pl-s1"},{"start":50,"end":51,"cssClass":"pl-c1"},{"start":52,"end":53,"cssClass":"pl-c1"}],[{"start":5,"end":9,"cssClass":"pl-s1"},{"start":10,"end":15,"cssClass":"pl-s1"},{"start":16,"end":21,"cssClass":"pl-s1"},{"start":23,"end":25,"cssClass":"pl-c1"},{"start":26,"end":39,"cssClass":"pl-s1"}],[{"start":5,"end":11,"cssClass":"pl-k"},{"start":12,"end":16,"cssClass":"pl-c1"}],[],[],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":12,"cssClass":"pl-s1"}],[{"start":1,"end":4,"cssClass":"pl-k"},{"start":5,"end":13,"cssClass":"pl-en"},{"start":14,"end":18,"cssClass":"pl-s1"},{"start":19,"end":24,"cssClass":"pl-s1"},{"start":25,"end":29,"cssClass":"pl-s1"},{"start":30,"end":40,"cssClass":"pl-s1"},{"start":41,"end":46,"cssClass":"pl-s1"}],[{"start":2,"end":6,"cssClass":"pl-s1"},{"start":7,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":16,"cssClass":"pl-en"},{"start":17,"end":22,"cssClass":"pl-s1"},{"start":23,"end":26,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":28,"end":31,"cssClass":"pl-en"},{"start":32,"end":36,"cssClass":"pl-s1"},{"start":37,"end":40,"cssClass":"pl-s1"},{"start":41,"end":42,"cssClass":"pl-c1"},{"start":42,"end":45,"cssClass":"pl-en"},{"start":46,"end":52,"cssClass":"pl-s1"},{"start":53,"end":60,"cssClass":"pl-en"},{"start":61,"end":64,"cssClass":"pl-c1"},{"start":65,"end":68,"cssClass":"pl-c1"}],[{"start":2,"end":6,"cssClass":"pl-s1"},{"start":7,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":24,"cssClass":"pl-s1"},{"start":25,"end":28,"cssClass":"pl-s1"}],[{"start":2,"end":6,"cssClass":"pl-s1"},{"start":7,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":20,"cssClass":"pl-s1"}],[{"start":2,"end":6,"cssClass":"pl-s1"},{"start":7,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":17,"cssClass":"pl-s1"},{"start":18,"end":21,"cssClass":"pl-s1"}],[{"start":2,"end":6,"cssClass":"pl-s1"},{"start":7,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":25,"cssClass":"pl-s1"},{"start":26,"end":30,"cssClass":"pl-s1"}],[{"start":2,"end":6,"cssClass":"pl-s1"},{"start":7,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":23,"cssClass":"pl-s1"},{"start":24,"end":28,"cssClass":"pl-s1"}],[{"start":2,"end":6,"cssClass":"pl-s1"},{"start":7,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":30,"cssClass":"pl-s1"}],[{"start":2,"end":6,"cssClass":"pl-s1"},{"start":7,"end":14,"cssClass":"pl-s1"},{"start":15,"end":21,"cssClass":"pl-en"},{"start":23,"end":27,"cssClass":"pl-s1"},{"start":28,"end":31,"cssClass":"pl-s1"},{"start":34,"end":38,"cssClass":"pl-s1"}],[{"start":2,"end":13,"cssClass":"pl-s1"},{"start":14,"end":20,"cssClass":"pl-en"},{"start":22,"end":26,"cssClass":"pl-s1"},{"start":27,"end":30,"cssClass":"pl-s1"},{"start":33,"end":37,"cssClass":"pl-s1"}],[],[],[],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":10,"cssClass":"pl-s1"}],[{"start":1,"end":4,"cssClass":"pl-k"},{"start":5,"end":13,"cssClass":"pl-en"},{"start":14,"end":18,"cssClass":"pl-s1"},{"start":19,"end":22,"cssClass":"pl-s1"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":27,"end":31,"cssClass":"pl-s1"},{"start":32,"end":33,"cssClass":"pl-c1"},{"start":34,"end":36,"cssClass":"pl-s"},{"start":37,"end":45,"cssClass":"pl-s1"},{"start":46,"end":47,"cssClass":"pl-c1"},{"start":48,"end":50,"cssClass":"pl-s"},{"start":51,"end":59,"cssClass":"pl-s1"},{"start":60,"end":61,"cssClass":"pl-c1"},{"start":62,"end":64,"cssClass":"pl-s"},{"start":65,"end":68,"cssClass":"pl-s1"},{"start":69,"end":70,"cssClass":"pl-c1"},{"start":71,"end":73,"cssClass":"pl-s"}],[{"start":2,"end":6,"cssClass":"pl-s1"},{"start":7,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":16,"cssClass":"pl-s1"}],[{"start":2,"end":6,"cssClass":"pl-s1"},{"start":7,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":18,"cssClass":"pl-s1"}],[{"start":2,"end":6,"cssClass":"pl-s1"},{"start":7,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":20,"cssClass":"pl-s"}],[{"start":2,"end":6,"cssClass":"pl-s1"},{"start":7,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":20,"cssClass":"pl-s"}],[{"start":2,"end":6,"cssClass":"pl-s1"},{"start":7,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":16,"cssClass":"pl-s1"}],[{"start":2,"end":6,"cssClass":"pl-s1"},{"start":7,"end":14,"cssClass":"pl-s1"},{"start":15,"end":16,"cssClass":"pl-c1"}],[],[],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":15,"cssClass":"pl-s1"}],[{"start":1,"end":51,"cssClass":"pl-s"}],[{"start":0,"end":30,"cssClass":"pl-s"}],[{"start":1,"end":4,"cssClass":"pl-k"},{"start":5,"end":15,"cssClass":"pl-en"}],[{"start":2,"end":5,"cssClass":"pl-s1"},{"start":6,"end":7,"cssClass":"pl-c1"},{"start":8,"end":9,"cssClass":"pl-c1"}],[{"start":2,"end":5,"cssClass":"pl-k"}],[{"start":3,"end":6,"cssClass":"pl-s1"},{"start":7,"end":8,"cssClass":"pl-c1"},{"start":9,"end":12,"cssClass":"pl-en"},{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":41,"cssClass":"pl-s"}],[{"start":2,"end":8,"cssClass":"pl-k"},{"start":9,"end":19,"cssClass":"pl-v"}],[{"start":3,"end":8,"cssClass":"pl-en"},{"start":9,"end":41,"cssClass":"pl-s"}],[{"start":3,"end":9,"cssClass":"pl-k"},{"start":10,"end":19,"cssClass":"pl-s1"},{"start":20,"end":30,"cssClass":"pl-en"}],[{"start":2,"end":6,"cssClass":"pl-k"}],[{"start":3,"end":9,"cssClass":"pl-k"},{"start":10,"end":13,"cssClass":"pl-s1"}],[],[{"start":1,"end":4,"cssClass":"pl-k"},{"start":5,"end":15,"cssClass":"pl-en"}],[{"start":2,"end":5,"cssClass":"pl-s1"},{"start":6,"end":7,"cssClass":"pl-c1"},{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":38,"cssClass":"pl-s"}],[{"start":2,"end":8,"cssClass":"pl-k"},{"start":9,"end":12,"cssClass":"pl-s1"}],[],[],[{"start":1,"end":4,"cssClass":"pl-k"},{"start":5,"end":24,"cssClass":"pl-en"}],[{"start":2,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":15,"cssClass":"pl-c1"}],[{"start":2,"end":5,"cssClass":"pl-k"}],[{"start":3,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":18,"cssClass":"pl-en"},{"start":19,"end":24,"cssClass":"pl-en"},{"start":25,"end":53,"cssClass":"pl-s"}],[{"start":2,"end":8,"cssClass":"pl-k"},{"start":9,"end":19,"cssClass":"pl-v"}],[{"start":3,"end":8,"cssClass":"pl-en"},{"start":9,"end":46,"cssClass":"pl-s"}],[{"start":3,"end":9,"cssClass":"pl-k"},{"start":10,"end":19,"cssClass":"pl-s1"},{"start":20,"end":39,"cssClass":"pl-en"}],[{"start":2,"end":6,"cssClass":"pl-k"}],[{"start":3,"end":5,"cssClass":"pl-k"},{"start":6,"end":15,"cssClass":"pl-s1"},{"start":16,"end":19,"cssClass":"pl-c1"},{"start":20,"end":22,"cssClass":"pl-c1"},{"start":23,"end":29,"cssClass":"pl-s1"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":46,"cssClass":"pl-s"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":20,"cssClass":"pl-s1"},{"start":21,"end":40,"cssClass":"pl-en"}],[{"start":3,"end":7,"cssClass":"pl-k"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":20,"cssClass":"pl-s1"}],[],[],[],[{"start":1,"end":4,"cssClass":"pl-k"},{"start":5,"end":23,"cssClass":"pl-en"}],[{"start":2,"end":8,"cssClass":"pl-s1"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":11,"end":16,"cssClass":"pl-en"},{"start":17,"end":40,"cssClass":"pl-s"}],[{"start":2,"end":4,"cssClass":"pl-k"},{"start":5,"end":11,"cssClass":"pl-s1"},{"start":12,"end":15,"cssClass":"pl-c1"},{"start":16,"end":18,"cssClass":"pl-c1"},{"start":20,"end":23,"cssClass":"pl-s"},{"start":24,"end":27,"cssClass":"pl-s"},{"start":28,"end":31,"cssClass":"pl-s"},{"start":32,"end":35,"cssClass":"pl-s"},{"start":36,"end":39,"cssClass":"pl-s"},{"start":40,"end":43,"cssClass":"pl-s"},{"start":44,"end":47,"cssClass":"pl-s"},{"start":48,"end":51,"cssClass":"pl-s"}],[{"start":3,"end":8,"cssClass":"pl-en"},{"start":9,"end":39,"cssClass":"pl-s"}],[{"start":3,"end":9,"cssClass":"pl-k"},{"start":10,"end":19,"cssClass":"pl-s1"},{"start":20,"end":38,"cssClass":"pl-en"}],[{"start":2,"end":6,"cssClass":"pl-k"}],[{"start":3,"end":9,"cssClass":"pl-k"},{"start":10,"end":13,"cssClass":"pl-en"},{"start":14,"end":20,"cssClass":"pl-s1"}],[],[{"start":1,"end":4,"cssClass":"pl-k"},{"start":5,"end":17,"cssClass":"pl-en"}],[{"start":2,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":15,"cssClass":"pl-en"},{"start":16,"end":37,"cssClass":"pl-s"}],[{"start":2,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":15,"cssClass":"pl-s1"},{"start":16,"end":21,"cssClass":"pl-en"}],[{"start":2,"end":4,"cssClass":"pl-k"},{"start":5,"end":10,"cssClass":"pl-s1"},{"start":11,"end":14,"cssClass":"pl-c1"},{"start":15,"end":17,"cssClass":"pl-c1"},{"start":19,"end":23,"cssClass":"pl-s"},{"start":24,"end":29,"cssClass":"pl-s"},{"start":30,"end":35,"cssClass":"pl-s"}],[{"start":3,"end":8,"cssClass":"pl-en"},{"start":9,"end":39,"cssClass":"pl-s"}],[{"start":3,"end":9,"cssClass":"pl-k"},{"start":10,"end":19,"cssClass":"pl-s1"},{"start":20,"end":32,"cssClass":"pl-en"}],[{"start":2,"end":6,"cssClass":"pl-k"}],[{"start":3,"end":9,"cssClass":"pl-k"},{"start":10,"end":15,"cssClass":"pl-s1"}],[],[{"start":1,"end":4,"cssClass":"pl-k"},{"start":5,"end":18,"cssClass":"pl-en"}],[{"start":2,"end":8,"cssClass":"pl-s1"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":11,"end":16,"cssClass":"pl-en"},{"start":17,"end":36,"cssClass":"pl-s"}],[{"start":2,"end":4,"cssClass":"pl-k"},{"start":5,"end":11,"cssClass":"pl-s1"},{"start":12,"end":15,"cssClass":"pl-c1"},{"start":16,"end":18,"cssClass":"pl-c1"},{"start":20,"end":23,"cssClass":"pl-s"},{"start":24,"end":27,"cssClass":"pl-s"}],[{"start":3,"end":8,"cssClass":"pl-en"},{"start":9,"end":38,"cssClass":"pl-s"}],[{"start":3,"end":9,"cssClass":"pl-k"},{"start":10,"end":19,"cssClass":"pl-s1"},{"start":20,"end":33,"cssClass":"pl-en"}],[{"start":2,"end":8,"cssClass":"pl-k"},{"start":9,"end":15,"cssClass":"pl-s1"}],[],[{"start":1,"end":4,"cssClass":"pl-k"},{"start":5,"end":22,"cssClass":"pl-en"}],[{"start":2,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":16,"cssClass":"pl-c1"}],[{"start":2,"end":5,"cssClass":"pl-k"}],[{"start":3,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":19,"cssClass":"pl-en"},{"start":20,"end":25,"cssClass":"pl-en"},{"start":26,"end":59,"cssClass":"pl-s"}],[{"start":3,"end":5,"cssClass":"pl-k"},{"start":6,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":20,"cssClass":"pl-c1"}],[{"start":4,"end":9,"cssClass":"pl-k"},{"start":10,"end":20,"cssClass":"pl-v"}],[{"start":2,"end":8,"cssClass":"pl-k"},{"start":9,"end":19,"cssClass":"pl-v"}],[{"start":3,"end":8,"cssClass":"pl-en"},{"start":9,"end":38,"cssClass":"pl-s"}],[{"start":3,"end":9,"cssClass":"pl-k"},{"start":10,"end":19,"cssClass":"pl-s1"},{"start":20,"end":37,"cssClass":"pl-en"}],[{"start":2,"end":6,"cssClass":"pl-k"}],[{"start":3,"end":9,"cssClass":"pl-k"},{"start":10,"end":20,"cssClass":"pl-s1"}],[{"start":1,"end":4,"cssClass":"pl-k"},{"start":5,"end":15,"cssClass":"pl-en"}],[{"start":2,"end":5,"cssClass":"pl-s1"},{"start":6,"end":7,"cssClass":"pl-c1"},{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":41,"cssClass":"pl-s"}],[{"start":2,"end":4,"cssClass":"pl-k"},{"start":5,"end":8,"cssClass":"pl-s1"},{"start":9,"end":12,"cssClass":"pl-c1"},{"start":13,"end":15,"cssClass":"pl-c1"},{"start":16,"end":27,"cssClass":"pl-s1"}],[{"start":3,"end":8,"cssClass":"pl-en"},{"start":9,"end":45,"cssClass":"pl-s"}],[{"start":3,"end":9,"cssClass":"pl-k"},{"start":10,"end":19,"cssClass":"pl-s1"},{"start":20,"end":30,"cssClass":"pl-en"}],[{"start":2,"end":6,"cssClass":"pl-k"}],[{"start":3,"end":9,"cssClass":"pl-k"},{"start":10,"end":13,"cssClass":"pl-s1"}],[],[],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":15,"cssClass":"pl-en"}],[{"start":1,"end":3,"cssClass":"pl-k"},{"start":4,"end":7,"cssClass":"pl-c1"},{"start":8,"end":17,"cssClass":"pl-s1"}],[{"start":2,"end":7,"cssClass":"pl-en"},{"start":8,"end":11,"cssClass":"pl-s"}],[],[{"start":1,"end":23,"cssClass":"pl-en"},{"start":24,"end":27,"cssClass":"pl-s"}],[{"start":1,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":19,"cssClass":"pl-s1"},{"start":20,"end":39,"cssClass":"pl-en"}],[{"start":1,"end":7,"cssClass":"pl-s1"},{"start":8,"end":14,"cssClass":"pl-s1"},{"start":16,"end":38,"cssClass":"pl-en"}],[{"start":1,"end":6,"cssClass":"pl-s1"},{"start":7,"end":8,"cssClass":"pl-c1"},{"start":9,"end":18,"cssClass":"pl-s1"},{"start":19,"end":31,"cssClass":"pl-en"}],[{"start":1,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":23,"cssClass":"pl-s1"},{"start":24,"end":41,"cssClass":"pl-en"}],[{"start":1,"end":3,"cssClass":"pl-k"},{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":17,"cssClass":"pl-s1"},{"start":19,"end":36,"cssClass":"pl-en"},{"start":37,"end":42,"cssClass":"pl-s1"},{"start":43,"end":53,"cssClass":"pl-s1"}],[{"start":2,"end":7,"cssClass":"pl-en"},{"start":8,"end":29,"cssClass":"pl-s"},{"start":30,"end":36,"cssClass":"pl-s1"},{"start":37,"end":43,"cssClass":"pl-s1"},{"start":45,"end":49,"cssClass":"pl-s1"},{"start":50,"end":55,"cssClass":"pl-s1"},{"start":56,"end":57,"cssClass":"pl-c1"},{"start":57,"end":67,"cssClass":"pl-s1"},{"start":68,"end":72,"cssClass":"pl-s"}],[{"start":2,"end":8,"cssClass":"pl-s1"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":11,"end":20,"cssClass":"pl-s1"},{"start":21,"end":34,"cssClass":"pl-en"}],[{"start":2,"end":4,"cssClass":"pl-k"},{"start":5,"end":11,"cssClass":"pl-s1"},{"start":12,"end":14,"cssClass":"pl-c1"},{"start":15,"end":18,"cssClass":"pl-s"}],[{"start":3,"end":9,"cssClass":"pl-s1"},{"start":10,"end":16,"cssClass":"pl-s1"},{"start":18,"end":29,"cssClass":"pl-en"},{"start":30,"end":35,"cssClass":"pl-s1"},{"start":36,"end":46,"cssClass":"pl-s1"}],[{"start":3,"end":8,"cssClass":"pl-en"},{"start":9,"end":34,"cssClass":"pl-s"},{"start":29,"end":31,"cssClass":"pl-cce"},{"start":31,"end":33,"cssClass":"pl-cce"}],[{"start":3,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":16,"cssClass":"pl-en"},{"start":17,"end":23,"cssClass":"pl-s1"},{"start":24,"end":30,"cssClass":"pl-s1"},{"start":32,"end":37,"cssClass":"pl-s1"},{"start":38,"end":41,"cssClass":"pl-s1"},{"start":43,"end":53,"cssClass":"pl-s1"},{"start":54,"end":59,"cssClass":"pl-s1"}],[{"start":3,"end":8,"cssClass":"pl-en"},{"start":9,"end":37,"cssClass":"pl-s"},{"start":38,"end":42,"cssClass":"pl-s1"},{"start":43,"end":46,"cssClass":"pl-s1"},{"start":47,"end":53,"cssClass":"pl-s"},{"start":48,"end":50,"cssClass":"pl-cce"},{"start":50,"end":52,"cssClass":"pl-cce"}],[{"start":3,"end":7,"cssClass":"pl-en"}],[{"start":2,"end":6,"cssClass":"pl-k"}],[{"start":3,"end":8,"cssClass":"pl-en"},{"start":9,"end":25,"cssClass":"pl-s"},{"start":20,"end":22,"cssClass":"pl-cce"},{"start":22,"end":24,"cssClass":"pl-cce"}],[{"start":3,"end":7,"cssClass":"pl-en"}],[{"start":1,"end":5,"cssClass":"pl-k"}],[{"start":2,"end":7,"cssClass":"pl-en"},{"start":8,"end":18,"cssClass":"pl-s1"},{"start":19,"end":43,"cssClass":"pl-s"}],[{"start":2,"end":6,"cssClass":"pl-en"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":17,"cssClass":"pl-en"}],[{"start":1,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":16,"cssClass":"pl-s1"},{"start":17,"end":27,"cssClass":"pl-en"}],[{"start":1,"end":3,"cssClass":"pl-k"},{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":10,"cssClass":"pl-c1"},{"start":11,"end":22,"cssClass":"pl-s1"}],[{"start":2,"end":11,"cssClass":"pl-en"},{"start":12,"end":15,"cssClass":"pl-s1"}],[{"start":2,"end":7,"cssClass":"pl-en"},{"start":8,"end":29,"cssClass":"pl-s"}],[{"start":2,"end":8,"cssClass":"pl-s1"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":11,"end":20,"cssClass":"pl-s1"},{"start":21,"end":34,"cssClass":"pl-en"}],[{"start":2,"end":4,"cssClass":"pl-k"},{"start":5,"end":11,"cssClass":"pl-s1"},{"start":12,"end":14,"cssClass":"pl-c1"},{"start":15,"end":18,"cssClass":"pl-s"}],[{"start":3,"end":5,"cssClass":"pl-k"},{"start":6,"end":15,"cssClass":"pl-s1"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":31,"cssClass":"pl-s"},{"start":28,"end":30,"cssClass":"pl-cce"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":22,"cssClass":"pl-s1"},{"start":23,"end":26,"cssClass":"pl-s1"},{"start":28,"end":37,"cssClass":"pl-s1"},{"start":39,"end":44,"cssClass":"pl-s1"},{"start":45,"end":56,"cssClass":"pl-s1"},{"start":57,"end":60,"cssClass":"pl-s1"},{"start":62,"end":67,"cssClass":"pl-s1"},{"start":69,"end":71,"cssClass":"pl-c1"},{"start":72,"end":83,"cssClass":"pl-s1"},{"start":84,"end":87,"cssClass":"pl-s1"},{"start":89,"end":99,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":13,"cssClass":"pl-s1"},{"start":14,"end":25,"cssClass":"pl-s1"},{"start":26,"end":29,"cssClass":"pl-s1"},{"start":31,"end":34,"cssClass":"pl-s1"},{"start":36,"end":43,"cssClass":"pl-s1"},{"start":44,"end":47,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":19,"cssClass":"pl-s1"},{"start":20,"end":23,"cssClass":"pl-s1"}],[{"start":3,"end":7,"cssClass":"pl-k"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":13,"cssClass":"pl-s"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":31,"cssClass":"pl-s"},{"start":28,"end":30,"cssClass":"pl-cce"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":22,"cssClass":"pl-s1"},{"start":23,"end":26,"cssClass":"pl-s1"},{"start":28,"end":37,"cssClass":"pl-s1"},{"start":39,"end":44,"cssClass":"pl-s1"},{"start":45,"end":56,"cssClass":"pl-s1"},{"start":57,"end":60,"cssClass":"pl-s1"},{"start":62,"end":67,"cssClass":"pl-s1"},{"start":69,"end":71,"cssClass":"pl-c1"},{"start":72,"end":83,"cssClass":"pl-s1"},{"start":84,"end":87,"cssClass":"pl-s1"},{"start":89,"end":99,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":13,"cssClass":"pl-s1"},{"start":14,"end":25,"cssClass":"pl-s1"},{"start":26,"end":29,"cssClass":"pl-s1"},{"start":31,"end":34,"cssClass":"pl-s1"},{"start":36,"end":43,"cssClass":"pl-s1"},{"start":44,"end":47,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":19,"cssClass":"pl-s1"},{"start":20,"end":23,"cssClass":"pl-s1"}],[{"start":2,"end":6,"cssClass":"pl-k"}],[{"start":3,"end":8,"cssClass":"pl-en"},{"start":9,"end":35,"cssClass":"pl-s"},{"start":10,"end":12,"cssClass":"pl-cce"},{"start":32,"end":34,"cssClass":"pl-cce"}],[{"start":1,"end":5,"cssClass":"pl-en"}],[],[],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":26,"cssClass":"pl-en"},{"start":27,"end":31,"cssClass":"pl-s1"},{"start":32,"end":33,"cssClass":"pl-c1"},{"start":34,"end":36,"cssClass":"pl-s"}],[{"start":1,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":12,"cssClass":"pl-en"},{"start":13,"end":42,"cssClass":"pl-s"}],[{"start":1,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":12,"cssClass":"pl-en"},{"start":13,"end":47,"cssClass":"pl-s"}],[{"start":1,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":11,"cssClass":"pl-c1"}],[{"start":1,"end":4,"cssClass":"pl-k"},{"start":5,"end":6,"cssClass":"pl-s1"},{"start":7,"end":9,"cssClass":"pl-c1"},{"start":10,"end":16,"cssClass":"pl-s1"}],[{"start":2,"end":4,"cssClass":"pl-k"},{"start":5,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":15,"end":18,"cssClass":"pl-s1"},{"start":19,"end":21,"cssClass":"pl-c1"},{"start":22,"end":25,"cssClass":"pl-s1"},{"start":26,"end":29,"cssClass":"pl-c1"},{"start":30,"end":36,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-s1"},{"start":40,"end":43,"cssClass":"pl-s1"},{"start":44,"end":46,"cssClass":"pl-c1"},{"start":47,"end":50,"cssClass":"pl-s1"}],[{"start":3,"end":8,"cssClass":"pl-en"},{"start":9,"end":25,"cssClass":"pl-s"},{"start":26,"end":32,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-s1"},{"start":36,"end":40,"cssClass":"pl-s1"},{"start":42,"end":45,"cssClass":"pl-s"},{"start":47,"end":56,"cssClass":"pl-s"},{"start":57,"end":63,"cssClass":"pl-s1"},{"start":64,"end":65,"cssClass":"pl-s1"},{"start":67,"end":70,"cssClass":"pl-s1"},{"start":72,"end":75,"cssClass":"pl-s"},{"start":76,"end":95,"cssClass":"pl-s"},{"start":96,"end":102,"cssClass":"pl-s1"},{"start":103,"end":104,"cssClass":"pl-s1"},{"start":106,"end":119,"cssClass":"pl-s1"}],[{"start":3,"end":9,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":13,"end":14,"cssClass":"pl-c1"}],[{"start":1,"end":3,"cssClass":"pl-k"},{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":13,"cssClass":"pl-c1"},{"start":14,"end":15,"cssClass":"pl-c1"}],[{"start":2,"end":7,"cssClass":"pl-en"},{"start":8,"end":63,"cssClass":"pl-s"},{"start":9,"end":11,"cssClass":"pl-cce"},{"start":60,"end":62,"cssClass":"pl-cce"}],[{"start":2,"end":6,"cssClass":"pl-en"}],[{"start":1,"end":3,"cssClass":"pl-k"},{"start":4,"end":8,"cssClass":"pl-s1"},{"start":9,"end":11,"cssClass":"pl-c1"},{"start":12,"end":14,"cssClass":"pl-s"}],[{"start":2,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":23,"cssClass":"pl-s1"},{"start":24,"end":43,"cssClass":"pl-en"}],[{"start":2,"end":8,"cssClass":"pl-s1"},{"start":9,"end":18,"cssClass":"pl-s1"},{"start":20,"end":42,"cssClass":"pl-en"}],[{"start":2,"end":6,"cssClass":"pl-en"}],[{"start":1,"end":5,"cssClass":"pl-k"}],[{"start":2,"end":6,"cssClass":"pl-k"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":13,"cssClass":"pl-en"},{"start":14,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":22,"cssClass":"pl-s"}],[{"start":1,"end":3,"cssClass":"pl-k"},{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":10,"cssClass":"pl-c1"},{"start":11,"end":13,"cssClass":"pl-s"}],[{"start":2,"end":5,"cssClass":"pl-s1"},{"start":6,"end":7,"cssClass":"pl-c1"},{"start":8,"end":17,"cssClass":"pl-s1"},{"start":18,"end":28,"cssClass":"pl-en"}],[{"start":2,"end":7,"cssClass":"pl-en"}],[{"start":2,"end":7,"cssClass":"pl-en"},{"start":8,"end":22,"cssClass":"pl-s"},{"start":23,"end":34,"cssClass":"pl-s1"},{"start":35,"end":38,"cssClass":"pl-s1"},{"start":40,"end":49,"cssClass":"pl-s1"}],[{"start":2,"end":7,"cssClass":"pl-en"},{"start":8,"end":23,"cssClass":"pl-s"},{"start":24,"end":35,"cssClass":"pl-s1"},{"start":36,"end":39,"cssClass":"pl-s1"},{"start":41,"end":51,"cssClass":"pl-s1"}],[{"start":2,"end":7,"cssClass":"pl-en"},{"start":8,"end":25,"cssClass":"pl-s"},{"start":26,"end":37,"cssClass":"pl-s1"},{"start":38,"end":41,"cssClass":"pl-s1"},{"start":43,"end":52,"cssClass":"pl-s1"},{"start":53,"end":65,"cssClass":"pl-s"},{"start":66,"end":72,"cssClass":"pl-s1"},{"start":73,"end":84,"cssClass":"pl-s1"},{"start":85,"end":88,"cssClass":"pl-s1"},{"start":90,"end":99,"cssClass":"pl-s1"},{"start":101,"end":104,"cssClass":"pl-s1"},{"start":105,"end":122,"cssClass":"pl-s"},{"start":123,"end":129,"cssClass":"pl-s1"},{"start":130,"end":141,"cssClass":"pl-s1"},{"start":142,"end":145,"cssClass":"pl-s1"},{"start":147,"end":156,"cssClass":"pl-s1"},{"start":158,"end":161,"cssClass":"pl-s1"}],[{"start":2,"end":7,"cssClass":"pl-en"},{"start":8,"end":35,"cssClass":"pl-s"},{"start":36,"end":47,"cssClass":"pl-s1"},{"start":48,"end":51,"cssClass":"pl-s1"},{"start":53,"end":63,"cssClass":"pl-s1"}],[{"start":2,"end":7,"cssClass":"pl-en"}],[{"start":2,"end":6,"cssClass":"pl-en"}],[{"start":1,"end":5,"cssClass":"pl-k"}],[{"start":2,"end":7,"cssClass":"pl-en"}],[{"start":2,"end":7,"cssClass":"pl-en"},{"start":8,"end":22,"cssClass":"pl-s"},{"start":23,"end":34,"cssClass":"pl-s1"},{"start":35,"end":38,"cssClass":"pl-s1"},{"start":40,"end":49,"cssClass":"pl-s1"}],[{"start":2,"end":7,"cssClass":"pl-en"},{"start":8,"end":23,"cssClass":"pl-s"},{"start":24,"end":35,"cssClass":"pl-s1"},{"start":36,"end":39,"cssClass":"pl-s1"},{"start":41,"end":51,"cssClass":"pl-s1"}],[{"start":2,"end":7,"cssClass":"pl-en"},{"start":8,"end":25,"cssClass":"pl-s"},{"start":26,"end":37,"cssClass":"pl-s1"},{"start":38,"end":41,"cssClass":"pl-s1"},{"start":43,"end":52,"cssClass":"pl-s1"},{"start":53,"end":65,"cssClass":"pl-s"},{"start":66,"end":72,"cssClass":"pl-s1"},{"start":73,"end":84,"cssClass":"pl-s1"},{"start":85,"end":88,"cssClass":"pl-s1"},{"start":90,"end":99,"cssClass":"pl-s1"},{"start":101,"end":104,"cssClass":"pl-s1"},{"start":105,"end":122,"cssClass":"pl-s"},{"start":123,"end":129,"cssClass":"pl-s1"},{"start":130,"end":141,"cssClass":"pl-s1"},{"start":142,"end":145,"cssClass":"pl-s1"},{"start":147,"end":156,"cssClass":"pl-s1"},{"start":158,"end":161,"cssClass":"pl-s1"}],[{"start":2,"end":7,"cssClass":"pl-en"},{"start":8,"end":35,"cssClass":"pl-s"},{"start":36,"end":47,"cssClass":"pl-s1"},{"start":48,"end":51,"cssClass":"pl-s1"},{"start":53,"end":63,"cssClass":"pl-s1"}],[{"start":2,"end":7,"cssClass":"pl-en"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":18,"cssClass":"pl-en"}],[{"start":1,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":44,"cssClass":"pl-s"}],[{"start":1,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":12,"cssClass":"pl-en"},{"start":13,"end":38,"cssClass":"pl-s"}],[{"start":1,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":13,"cssClass":"pl-s1"},{"start":14,"end":21,"cssClass":"pl-en"},{"start":22,"end":26,"cssClass":"pl-c1"},{"start":27,"end":31,"cssClass":"pl-c1"}],[{"start":1,"end":9,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":43,"cssClass":"pl-s"}],[{"start":1,"end":9,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":47,"cssClass":"pl-s"}],[{"start":1,"end":2,"cssClass":"pl-s1"},{"start":3,"end":4,"cssClass":"pl-c1"},{"start":5,"end":9,"cssClass":"pl-en"},{"start":10,"end":13,"cssClass":"pl-s1"},{"start":15,"end":24,"cssClass":"pl-s1"},{"start":26,"end":34,"cssClass":"pl-s1"},{"start":36,"end":44,"cssClass":"pl-s1"},{"start":46,"end":49,"cssClass":"pl-s1"}],[{"start":1,"end":6,"cssClass":"pl-en"},{"start":7,"end":28,"cssClass":"pl-s"},{"start":29,"end":32,"cssClass":"pl-s1"}],[{"start":1,"end":6,"cssClass":"pl-s1"},{"start":7,"end":13,"cssClass":"pl-en"},{"start":15,"end":16,"cssClass":"pl-s1"},{"start":17,"end":20,"cssClass":"pl-s1"},{"start":23,"end":24,"cssClass":"pl-s1"}],[{"start":1,"end":5,"cssClass":"pl-en"}],[],[],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":14,"cssClass":"pl-s1"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":17,"end":19,"cssClass":"pl-s"}],[{"start":1,"end":7,"cssClass":"pl-k"},{"start":8,"end":11,"cssClass":"pl-s1"}],[{"start":1,"end":7,"cssClass":"pl-k"},{"start":8,"end":11,"cssClass":"pl-s1"}],[{"start":1,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":16,"cssClass":"pl-s1"},{"start":17,"end":27,"cssClass":"pl-en"}],[{"start":1,"end":4,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":16,"cssClass":"pl-s1"},{"start":17,"end":27,"cssClass":"pl-en"}],[{"start":1,"end":3,"cssClass":"pl-k"},{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":10,"cssClass":"pl-c1"},{"start":11,"end":16,"cssClass":"pl-s1"},{"start":17,"end":20,"cssClass":"pl-c1"},{"start":21,"end":26,"cssClass":"pl-s1"},{"start":27,"end":30,"cssClass":"pl-s1"},{"start":32,"end":35,"cssClass":"pl-s1"},{"start":36,"end":38,"cssClass":"pl-c1"},{"start":39,"end":42,"cssClass":"pl-s1"}],[{"start":2,"end":7,"cssClass":"pl-en"},{"start":8,"end":20,"cssClass":"pl-s"},{"start":9,"end":11,"cssClass":"pl-cce"},{"start":21,"end":26,"cssClass":"pl-s1"},{"start":27,"end":30,"cssClass":"pl-s1"},{"start":32,"end":36,"cssClass":"pl-s1"},{"start":37,"end":43,"cssClass":"pl-s"},{"start":40,"end":42,"cssClass":"pl-cce"}],[{"start":2,"end":8,"cssClass":"pl-k"},{"start":9,"end":18,"cssClass":"pl-s1"}],[{"start":2,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":18,"cssClass":"pl-c1"}],[{"start":1,"end":5,"cssClass":"pl-k"}],[{"start":2,"end":7,"cssClass":"pl-en"},{"start":8,"end":48,"cssClass":"pl-s"},{"start":9,"end":11,"cssClass":"pl-cce"},{"start":45,"end":47,"cssClass":"pl-cce"}],[{"start":2,"end":8,"cssClass":"pl-k"},{"start":9,"end":14,"cssClass":"pl-en"}],[{"start":1,"end":3,"cssClass":"pl-k"},{"start":4,"end":8,"cssClass":"pl-s1"},{"start":9,"end":11,"cssClass":"pl-c1"},{"start":12,"end":14,"cssClass":"pl-s"}],[{"start":2,"end":6,"cssClass":"pl-en"}],[{"start":1,"end":5,"cssClass":"pl-k"}],[{"start":2,"end":6,"cssClass":"pl-k"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":23,"cssClass":"pl-en"}],[{"start":1,"end":3,"cssClass":"pl-k"},{"start":4,"end":7,"cssClass":"pl-c1"},{"start":8,"end":17,"cssClass":"pl-s1"}],[{"start":2,"end":7,"cssClass":"pl-en"},{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":1,"end":4,"cssClass":"pl-k"},{"start":5,"end":6,"cssClass":"pl-s1"},{"start":7,"end":9,"cssClass":"pl-c1"},{"start":10,"end":15,"cssClass":"pl-s1"},{"start":16,"end":19,"cssClass":"pl-s1"},{"start":21,"end":28,"cssClass":"pl-s1"}],[{"start":2,"end":7,"cssClass":"pl-en"},{"start":8,"end":25,"cssClass":"pl-s"},{"start":9,"end":11,"cssClass":"pl-cce"},{"start":26,"end":27,"cssClass":"pl-s1"}],[{"start":2,"end":11,"cssClass":"pl-en"},{"start":12,"end":13,"cssClass":"pl-s1"}],[{"start":1,"end":5,"cssClass":"pl-en"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":7,"cssClass":"pl-en"}],[{"start":1,"end":2,"cssClass":"pl-en"}],[{"start":1,"end":6,"cssClass":"pl-en"},{"start":7,"end":138,"cssClass":"pl-s"}],[{"start":1,"end":6,"cssClass":"pl-en"},{"start":7,"end":138,"cssClass":"pl-s"}],[{"start":1,"end":4,"cssClass":"pl-s1"},{"start":5,"end":9,"cssClass":"pl-en"}],[],[],[{"start":0,"end":2,"cssClass":"pl-s1"},{"start":3,"end":4,"cssClass":"pl-c1"},{"start":5,"end":10,"cssClass":"pl-en"},{"start":11,"end":27,"cssClass":"pl-s"},{"start":28,"end":33,"cssClass":"pl-c1"},{"start":34,"end":41,"cssClass":"pl-s"},{"start":42,"end":49,"cssClass":"pl-s"},{"start":50,"end":55,"cssClass":"pl-s"},{"start":56,"end":61,"cssClass":"pl-s"},{"start":62,"end":67,"cssClass":"pl-s"},{"start":68,"end":70,"cssClass":"pl-c1"},{"start":71,"end":73,"cssClass":"pl-c1"},{"start":74,"end":76,"cssClass":"pl-c1"},{"start":77,"end":81,"cssClass":"pl-c1"},{"start":82,"end":85,"cssClass":"pl-c1"},{"start":86,"end":89,"cssClass":"pl-c1"}],[{"start":0,"end":2,"cssClass":"pl-s1"},{"start":3,"end":4,"cssClass":"pl-c1"},{"start":5,"end":10,"cssClass":"pl-en"},{"start":11,"end":20,"cssClass":"pl-s"},{"start":21,"end":26,"cssClass":"pl-c1"},{"start":27,"end":34,"cssClass":"pl-s"},{"start":35,"end":42,"cssClass":"pl-s"},{"start":43,"end":48,"cssClass":"pl-s"},{"start":49,"end":54,"cssClass":"pl-s"},{"start":55,"end":60,"cssClass":"pl-s"},{"start":61,"end":63,"cssClass":"pl-c1"},{"start":64,"end":65,"cssClass":"pl-c1"},{"start":66,"end":68,"cssClass":"pl-c1"},{"start":69,"end":73,"cssClass":"pl-c1"},{"start":74,"end":77,"cssClass":"pl-c1"},{"start":78,"end":81,"cssClass":"pl-c1"}],[{"start":0,"end":2,"cssClass":"pl-s1"},{"start":3,"end":4,"cssClass":"pl-c1"},{"start":5,"end":10,"cssClass":"pl-en"},{"start":11,"end":26,"cssClass":"pl-s"},{"start":27,"end":32,"cssClass":"pl-c1"},{"start":33,"end":40,"cssClass":"pl-s"},{"start":41,"end":48,"cssClass":"pl-s"},{"start":49,"end":54,"cssClass":"pl-s"},{"start":55,"end":60,"cssClass":"pl-s"},{"start":61,"end":66,"cssClass":"pl-s"},{"start":67,"end":69,"cssClass":"pl-c1"},{"start":70,"end":72,"cssClass":"pl-c1"},{"start":73,"end":75,"cssClass":"pl-c1"},{"start":76,"end":79,"cssClass":"pl-c1"},{"start":80,"end":83,"cssClass":"pl-c1"},{"start":84,"end":87,"cssClass":"pl-c1"}],[{"start":0,"end":6,"cssClass":"pl-s1"},{"start":7,"end":8,"cssClass":"pl-c1"},{"start":10,"end":12,"cssClass":"pl-s1"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":17,"end":19,"cssClass":"pl-s1"},{"start":20,"end":22,"cssClass":"pl-s1"},{"start":23,"end":26,"cssClass":"pl-s1"},{"start":27,"end":29,"cssClass":"pl-s1"},{"start":30,"end":32,"cssClass":"pl-s1"},{"start":33,"end":36,"cssClass":"pl-s1"},{"start":37,"end":39,"cssClass":"pl-s1"}],[{"start":0,"end":2,"cssClass":"pl-s1"},{"start":3,"end":4,"cssClass":"pl-c1"},{"start":5,"end":9,"cssClass":"pl-en"},{"start":10,"end":14,"cssClass":"pl-c1"},{"start":15,"end":22,"cssClass":"pl-s"},{"start":23,"end":36,"cssClass":"pl-s"},{"start":37,"end":45,"cssClass":"pl-s"},{"start":46,"end":53,"cssClass":"pl-s"}],[{"start":0,"end":2,"cssClass":"pl-s1"},{"start":3,"end":4,"cssClass":"pl-c1"},{"start":5,"end":9,"cssClass":"pl-en"},{"start":10,"end":14,"cssClass":"pl-c1"},{"start":15,"end":25,"cssClass":"pl-s"},{"start":26,"end":32,"cssClass":"pl-s"},{"start":33,"end":41,"cssClass":"pl-s"},{"start":42,"end":51,"cssClass":"pl-s"}],[{"start":0,"end":5,"cssClass":"pl-s1"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":9,"cssClass":"pl-s1"},{"start":10,"end":13,"cssClass":"pl-s1"},{"start":16,"end":18,"cssClass":"pl-s1"},{"start":20,"end":22,"cssClass":"pl-s1"},{"start":23,"end":26,"cssClass":"pl-s1"},{"start":29,"end":31,"cssClass":"pl-s1"}],[{"start":0,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":8,"cssClass":"pl-en"}],[{"start":1,"end":7,"cssClass":"pl-k"},{"start":9,"end":15,"cssClass":"pl-s1"},{"start":16,"end":21,"cssClass":"pl-s1"},{"start":22,"end":33,"cssClass":"pl-s1"}],[{"start":1,"end":5,"cssClass":"pl-k"},{"start":6,"end":10,"cssClass":"pl-en"},{"start":11,"end":21,"cssClass":"pl-s"},{"start":22,"end":26,"cssClass":"pl-s"},{"start":28,"end":30,"cssClass":"pl-k"},{"start":31,"end":32,"cssClass":"pl-s1"}],[{"start":2,"end":8,"cssClass":"pl-s1"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":11,"end":17,"cssClass":"pl-s1"},{"start":18,"end":22,"cssClass":"pl-en"},{"start":23,"end":24,"cssClass":"pl-s1"}],[{"start":2,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":16,"cssClass":"pl-s1"},{"start":17,"end":21,"cssClass":"pl-en"},{"start":22,"end":23,"cssClass":"pl-s1"}],[{"start":2,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":22,"cssClass":"pl-s1"},{"start":23,"end":27,"cssClass":"pl-en"},{"start":28,"end":29,"cssClass":"pl-s1"}],[],[],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":5,"cssClass":"pl-en"}],[{"start":1,"end":5,"cssClass":"pl-k"},{"start":6,"end":10,"cssClass":"pl-en"},{"start":11,"end":21,"cssClass":"pl-s"},{"start":22,"end":26,"cssClass":"pl-s"},{"start":28,"end":30,"cssClass":"pl-k"},{"start":31,"end":32,"cssClass":"pl-s1"}],[{"start":2,"end":8,"cssClass":"pl-s1"},{"start":9,"end":13,"cssClass":"pl-en"},{"start":14,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-s1"}],[{"start":2,"end":8,"cssClass":"pl-s1"},{"start":9,"end":13,"cssClass":"pl-en"},{"start":14,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-s1"}],[{"start":2,"end":8,"cssClass":"pl-s1"},{"start":9,"end":13,"cssClass":"pl-en"},{"start":14,"end":25,"cssClass":"pl-s1"},{"start":26,"end":27,"cssClass":"pl-s1"}],[],[],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":10,"cssClass":"pl-s"},{"start":7,"end":9,"cssClass":"pl-cce"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":96,"cssClass":"pl-s"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":10,"cssClass":"pl-s"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":11,"end":13,"cssClass":"pl-c1"}],[{"start":0,"end":9,"cssClass":"pl-c"}],[],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":8,"cssClass":"pl-en"}],[{"start":1,"end":6,"cssClass":"pl-en"},{"start":7,"end":45,"cssClass":"pl-s"}],[{"start":1,"end":6,"cssClass":"pl-en"},{"start":7,"end":22,"cssClass":"pl-s"}],[{"start":1,"end":6,"cssClass":"pl-en"},{"start":7,"end":24,"cssClass":"pl-s"}],[{"start":1,"end":6,"cssClass":"pl-en"},{"start":7,"end":21,"cssClass":"pl-s"}],[{"start":1,"end":6,"cssClass":"pl-en"},{"start":7,"end":32,"cssClass":"pl-s"}],[{"start":1,"end":6,"cssClass":"pl-en"},{"start":7,"end":29,"cssClass":"pl-s"}],[{"start":1,"end":6,"cssClass":"pl-en"},{"start":7,"end":34,"cssClass":"pl-s"}],[{"start":1,"end":6,"cssClass":"pl-en"},{"start":7,"end":16,"cssClass":"pl-s"}],[{"start":1,"end":6,"cssClass":"pl-en"},{"start":7,"end":15,"cssClass":"pl-s"}],[{"start":1,"end":5,"cssClass":"pl-s1"},{"start":6,"end":7,"cssClass":"pl-c1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":14,"end":25,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":31,"end":44,"cssClass":"pl-s1"},{"start":46,"end":47,"cssClass":"pl-c1"},{"start":50,"end":59,"cssClass":"pl-s1"},{"start":61,"end":62,"cssClass":"pl-c1"},{"start":65,"end":87,"cssClass":"pl-s1"},{"start":89,"end":90,"cssClass":"pl-c1"},{"start":93,"end":107,"cssClass":"pl-s1"},{"start":109,"end":110,"cssClass":"pl-c1"},{"start":113,"end":132,"cssClass":"pl-s1"},{"start":134,"end":135,"cssClass":"pl-c1"},{"start":138,"end":143,"cssClass":"pl-s1"},{"start":145,"end":146,"cssClass":"pl-c1"},{"start":149,"end":152,"cssClass":"pl-s1"}],[{"start":1,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":19,"cssClass":"pl-s1"},{"start":20,"end":38,"cssClass":"pl-en"}],[{"start":1,"end":5,"cssClass":"pl-s1"},{"start":6,"end":12,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":4,"cssClass":"pl-en"}],[]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":null,"configFilePath":null,"networkDependabotPath":"/PowerstarPrasad/projects_5/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false,"repoAlertsPath":"/PowerstarPrasad/projects_5/security/dependabot","repoSecurityAndAnalysisPath":"/PowerstarPrasad/projects_5/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":true},"displayName":"railway project.py","displayUrl":"https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py?raw=true","headerInfo":{"blobSize":"9.33 KB","deleteInfo":{"deletePath":"https://github.com/PowerstarPrasad/projects_5/delete/main/railway%20project.py","deleteTooltip":"Delete this file"},"editInfo":{"editTooltip":"Edit this file"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"f8cc669","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FPowerstarPrasad%2Fprojects_5%2Fblob%2Fmain%2Frailway%2520project.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"322","truncatedSloc":"275"},"mode":"file"},"image":false,"isCodeownersFile":null,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","large":false,"loggedIn":true,"newDiscussionPath":"/PowerstarPrasad/projects_5/discussions/new","newIssuePath":"/PowerstarPrasad/projects_5/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/PowerstarPrasad/projects_5/blob/main/railway%20project.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/PowerstarPrasad/projects_5/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"PowerstarPrasad","repoName":"projects_5","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":null,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":false,"symbols":[{"name":"logged_in","kind":"constant","identStart":44,"identEnd":53,"extentStart":44,"extentEnd":61,"fullyQualifiedName":"logged_in","identUtf16":{"start":{"lineNumber":4,"utf16Col":0},"end":{"lineNumber":4,"utf16Col":9}},"extentUtf16":{"start":{"lineNumber":4,"utf16Col":0},"end":{"lineNumber":4,"utf16Col":17}}},{"name":"uid","kind":"constant","identStart":63,"identEnd":66,"extentStart":63,"extentEnd":70,"fullyQualifiedName":"uid","identUtf16":{"start":{"lineNumber":5,"utf16Col":0},"end":{"lineNumber":5,"utf16Col":3}},"extentUtf16":{"start":{"lineNumber":5,"utf16Col":0},"end":{"lineNumber":5,"utf16Col":7}}},{"name":"pwd","kind":"constant","identStart":72,"identEnd":75,"extentStart":72,"extentEnd":80,"fullyQualifiedName":"pwd","identUtf16":{"start":{"lineNumber":6,"utf16Col":0},"end":{"lineNumber":6,"utf16Col":3}},"extentUtf16":{"start":{"lineNumber":6,"utf16Col":0},"end":{"lineNumber":6,"utf16Col":8}}},{"name":"train","kind":"class","identStart":90,"identEnd":95,"extentStart":84,"extentEnd":1468,"fullyQualifiedName":"train","identUtf16":{"start":{"lineNumber":8,"utf16Col":6},"end":{"lineNumber":8,"utf16Col":11}},"extentUtf16":{"start":{"lineNumber":8,"utf16Col":0},"end":{"lineNumber":37,"utf16Col":16}}},{"name":"__init__","kind":"function","identStart":106,"identEnd":114,"extentStart":102,"extentEnd":718,"fullyQualifiedName":"train.__init__","identUtf16":{"start":{"lineNumber":9,"utf16Col":8},"end":{"lineNumber":9,"utf16Col":16}},"extentUtf16":{"start":{"lineNumber":9,"utf16Col":4},"end":{"lineNumber":18,"utf16Col":71}}},{"name":"print_seat_availablity","kind":"function","identStart":728,"identEnd":750,"extentStart":724,"extentEnd":971,"fullyQualifiedName":"train.print_seat_availablity","identUtf16":{"start":{"lineNumber":19,"utf16Col":8},"end":{"lineNumber":19,"utf16Col":30}},"extentUtf16":{"start":{"lineNumber":19,"utf16Col":4},"end":{"lineNumber":22,"utf16Col":68}}},{"name":"check_availabilty","kind":"function","identStart":981,"identEnd":998,"extentStart":977,"extentEnd":1352,"fullyQualifiedName":"train.check_availabilty","identUtf16":{"start":{"lineNumber":23,"utf16Col":8},"end":{"lineNumber":23,"utf16Col":25}},"extentUtf16":{"start":{"lineNumber":23,"utf16Col":4},"end":{"lineNumber":34,"utf16Col":19}}},{"name":"book_ticket","kind":"function","identStart":1362,"identEnd":1373,"extentStart":1358,"extentEnd":1468,"fullyQualifiedName":"train.book_ticket","identUtf16":{"start":{"lineNumber":35,"utf16Col":8},"end":{"lineNumber":35,"utf16Col":19}},"extentUtf16":{"start":{"lineNumber":35,"utf16Col":4},"end":{"lineNumber":37,"utf16Col":16}}},{"name":"ticket","kind":"class","identStart":1480,"identEnd":1486,"extentStart":1474,"extentEnd":1861,"fullyQualifiedName":"ticket","identUtf16":{"start":{"lineNumber":40,"utf16Col":6},"end":{"lineNumber":40,"utf16Col":12}},"extentUtf16":{"start":{"lineNumber":40,"utf16Col":0},"end":{"lineNumber":50,"utf16Col":39}}},{"name":"__init__","kind":"function","identStart":1494,"identEnd":1502,"extentStart":1490,"extentEnd":1861,"fullyQualifiedName":"ticket.__init__","identUtf16":{"start":{"lineNumber":41,"utf16Col":5},"end":{"lineNumber":41,"utf16Col":13}},"extentUtf16":{"start":{"lineNumber":41,"utf16Col":1},"end":{"lineNumber":50,"utf16Col":39}}},{"name":"user","kind":"class","identStart":1875,"identEnd":1879,"extentStart":1869,"extentEnd":2078,"fullyQualifiedName":"user","identUtf16":{"start":{"lineNumber":54,"utf16Col":6},"end":{"lineNumber":54,"utf16Col":10}},"extentUtf16":{"start":{"lineNumber":54,"utf16Col":0},"end":{"lineNumber":61,"utf16Col":19}}},{"name":"__init__","kind":"function","identStart":1887,"identEnd":1895,"extentStart":1883,"extentEnd":2078,"fullyQualifiedName":"user.__init__","identUtf16":{"start":{"lineNumber":55,"utf16Col":5},"end":{"lineNumber":55,"utf16Col":13}},"extentUtf16":{"start":{"lineNumber":55,"utf16Col":1},"end":{"lineNumber":61,"utf16Col":19}}},{"name":"acceptors","kind":"class","identStart":2090,"identEnd":2099,"extentStart":2084,"extentEnd":4035,"fullyQualifiedName":"acceptors","identUtf16":{"start":{"lineNumber":64,"utf16Col":6},"end":{"lineNumber":64,"utf16Col":15}},"extentUtf16":{"start":{"lineNumber":64,"utf16Col":0},"end":{"lineNumber":139,"utf16Col":13}}},{"name":"accept_uid","kind":"function","identStart":2191,"identEnd":2201,"extentStart":2187,"extentEnd":2392,"fullyQualifiedName":"acceptors.accept_uid","identUtf16":{"start":{"lineNumber":67,"utf16Col":5},"end":{"lineNumber":67,"utf16Col":15}},"extentUtf16":{"start":{"lineNumber":67,"utf16Col":1},"end":{"lineNumber":75,"utf16Col":13}}},{"name":"accept_pwd","kind":"function","identStart":2401,"identEnd":2411,"extentStart":2397,"extentEnd":2469,"fullyQualifiedName":"acceptors.accept_pwd","identUtf16":{"start":{"lineNumber":77,"utf16Col":5},"end":{"lineNumber":77,"utf16Col":15}},"extentUtf16":{"start":{"lineNumber":77,"utf16Col":1},"end":{"lineNumber":79,"utf16Col":12}}},{"name":"accept_train_number","kind":"function","identStart":2480,"identEnd":2499,"extentStart":2476,"extentEnd":2864,"fullyQualifiedName":"acceptors.accept_train_number","identUtf16":{"start":{"lineNumber":82,"utf16Col":5},"end":{"lineNumber":82,"utf16Col":24}},"extentUtf16":{"start":{"lineNumber":82,"utf16Col":1},"end":{"lineNumber":94,"utf16Col":20}}},{"name":"accept_menu_option","kind":"function","identStart":2878,"identEnd":2896,"extentStart":2874,"extentEnd":3113,"fullyQualifiedName":"acceptors.accept_menu_option","identUtf16":{"start":{"lineNumber":98,"utf16Col":5},"end":{"lineNumber":98,"utf16Col":23}},"extentUtf16":{"start":{"lineNumber":98,"utf16Col":1},"end":{"lineNumber":104,"utf16Col":21}}},{"name":"accept_coach","kind":"function","identStart":3122,"identEnd":3134,"extentStart":3118,"extentEnd":3345,"fullyQualifiedName":"acceptors.accept_coach","identUtf16":{"start":{"lineNumber":106,"utf16Col":5},"end":{"lineNumber":106,"utf16Col":17}},"extentUtf16":{"start":{"lineNumber":106,"utf16Col":1},"end":{"lineNumber":113,"utf16Col":15}}},{"name":"accept_prompt","kind":"function","identStart":3354,"identEnd":3367,"extentStart":3350,"extentEnd":3535,"fullyQualifiedName":"acceptors.accept_prompt","identUtf16":{"start":{"lineNumber":115,"utf16Col":5},"end":{"lineNumber":115,"utf16Col":18}},"extentUtf16":{"start":{"lineNumber":115,"utf16Col":1},"end":{"lineNumber":120,"utf16Col":15}}},{"name":"accept_ticket_num","kind":"function","identStart":3546,"identEnd":3563,"extentStart":3542,"extentEnd":3835,"fullyQualifiedName":"acceptors.accept_ticket_num","identUtf16":{"start":{"lineNumber":122,"utf16Col":5},"end":{"lineNumber":122,"utf16Col":22}},"extentUtf16":{"start":{"lineNumber":122,"utf16Col":1},"end":{"lineNumber":132,"utf16Col":20}}},{"name":"accept_pnr","kind":"function","identStart":3842,"identEnd":3852,"extentStart":3838,"extentEnd":4035,"fullyQualifiedName":"acceptors.accept_pnr","identUtf16":{"start":{"lineNumber":133,"utf16Col":5},"end":{"lineNumber":133,"utf16Col":15}},"extentUtf16":{"start":{"lineNumber":133,"utf16Col":1},"end":{"lineNumber":139,"utf16Col":13}}},{"name":"book_ticket","kind":"function","identStart":4047,"identEnd":4058,"extentStart":4043,"extentEnd":4810,"fullyQualifiedName":"book_ticket","identUtf16":{"start":{"lineNumber":143,"utf16Col":4},"end":{"lineNumber":143,"utf16Col":15}},"extentUtf16":{"start":{"lineNumber":143,"utf16Col":0},"end":{"lineNumber":166,"utf16Col":8}}},{"name":"cancel_ticket","kind":"function","identStart":4818,"identEnd":4831,"extentStart":4814,"extentEnd":5521,"fullyQualifiedName":"cancel_ticket","identUtf16":{"start":{"lineNumber":168,"utf16Col":4},"end":{"lineNumber":168,"utf16Col":17}},"extentUtf16":{"start":{"lineNumber":168,"utf16Col":0},"end":{"lineNumber":188,"utf16Col":7}}},{"name":"check_seat_availabilty","kind":"function","identStart":5533,"identEnd":5555,"extentStart":5529,"extentEnd":6115,"fullyQualifiedName":"check_seat_availabilty","identUtf16":{"start":{"lineNumber":192,"utf16Col":4},"end":{"lineNumber":192,"utf16Col":26}},"extentUtf16":{"start":{"lineNumber":192,"utf16Col":0},"end":{"lineNumber":208,"utf16Col":6}}},{"name":"check_pnr","kind":"function","identStart":6123,"identEnd":6132,"extentStart":6119,"extentEnd":6925,"fullyQualifiedName":"check_pnr","identUtf16":{"start":{"lineNumber":210,"utf16Col":4},"end":{"lineNumber":210,"utf16Col":13}},"extentUtf16":{"start":{"lineNumber":210,"utf16Col":0},"end":{"lineNumber":226,"utf16Col":9}}},{"name":"create_new_acc","kind":"function","identStart":6933,"identEnd":6947,"extentStart":6929,"extentEnd":7292,"fullyQualifiedName":"create_new_acc","identUtf16":{"start":{"lineNumber":228,"utf16Col":4},"end":{"lineNumber":228,"utf16Col":18}},"extentUtf16":{"start":{"lineNumber":228,"utf16Col":0},"end":{"lineNumber":237,"utf16Col":7}}},{"name":"login","kind":"function","identStart":7304,"identEnd":7309,"extentStart":7300,"extentEnd":7662,"fullyQualifiedName":"login","identUtf16":{"start":{"lineNumber":241,"utf16Col":4},"end":{"lineNumber":241,"utf16Col":9}},"extentUtf16":{"start":{"lineNumber":241,"utf16Col":0},"end":{"lineNumber":256,"utf16Col":6}}},{"name":"check_prev_bookings","kind":"function","identStart":7670,"identEnd":7689,"extentStart":7666,"extentEnd":7812,"fullyQualifiedName":"check_prev_bookings","identUtf16":{"start":{"lineNumber":258,"utf16Col":4},"end":{"lineNumber":258,"utf16Col":23}},"extentUtf16":{"start":{"lineNumber":258,"utf16Col":0},"end":{"lineNumber":264,"utf16Col":7}}},{"name":"end","kind":"function","identStart":7820,"identEnd":7823,"extentStart":7816,"extentEnd":8127,"fullyQualifiedName":"end","identUtf16":{"start":{"lineNumber":266,"utf16Col":4},"end":{"lineNumber":266,"utf16Col":7}},"extentUtf16":{"start":{"lineNumber":266,"utf16Col":0},"end":{"lineNumber":270,"utf16Col":11}}},{"name":"t1","kind":"constant","identStart":8133,"identEnd":8135,"extentStart":8133,"extentEnd":8223,"fullyQualifiedName":"t1","identUtf16":{"start":{"lineNumber":273,"utf16Col":0},"end":{"lineNumber":273,"utf16Col":2}},"extentUtf16":{"start":{"lineNumber":273,"utf16Col":0},"end":{"lineNumber":273,"utf16Col":90}}},{"name":"t2","kind":"constant","identStart":8225,"identEnd":8227,"extentStart":8225,"extentEnd":8307,"fullyQualifiedName":"t2","identUtf16":{"start":{"lineNumber":274,"utf16Col":0},"end":{"lineNumber":274,"utf16Col":2}},"extentUtf16":{"start":{"lineNumber":274,"utf16Col":0},"end":{"lineNumber":274,"utf16Col":82}}},{"name":"t3","kind":"constant","identStart":8309,"identEnd":8311,"extentStart":8309,"extentEnd":8397,"fullyQualifiedName":"t3","identUtf16":{"start":{"lineNumber":275,"utf16Col":0},"end":{"lineNumber":275,"utf16Col":2}},"extentUtf16":{"start":{"lineNumber":275,"utf16Col":0},"end":{"lineNumber":275,"utf16Col":88}}},{"name":"trains","kind":"constant","identStart":8399,"identEnd":8405,"extentStart":8399,"extentEnd":8439,"fullyQualifiedName":"trains","identUtf16":{"start":{"lineNumber":276,"utf16Col":0},"end":{"lineNumber":276,"utf16Col":6}},"extentUtf16":{"start":{"lineNumber":276,"utf16Col":0},"end":{"lineNumber":276,"utf16Col":40}}},{"name":"u1","kind":"constant","identStart":8441,"identEnd":8443,"extentStart":8441,"extentEnd":8495,"fullyQualifiedName":"u1","identUtf16":{"start":{"lineNumber":277,"utf16Col":0},"end":{"lineNumber":277,"utf16Col":2}},"extentUtf16":{"start":{"lineNumber":277,"utf16Col":0},"end":{"lineNumber":277,"utf16Col":54}}},{"name":"u2","kind":"constant","identStart":8497,"identEnd":8499,"extentStart":8497,"extentEnd":8549,"fullyQualifiedName":"u2","identUtf16":{"start":{"lineNumber":278,"utf16Col":0},"end":{"lineNumber":278,"utf16Col":2}},"extentUtf16":{"start":{"lineNumber":278,"utf16Col":0},"end":{"lineNumber":278,"utf16Col":52}}},{"name":"users","kind":"constant","identStart":8551,"identEnd":8556,"extentStart":8551,"extentEnd":8583,"fullyQualifiedName":"users","identUtf16":{"start":{"lineNumber":279,"utf16Col":0},"end":{"lineNumber":279,"utf16Col":5}},"extentUtf16":{"start":{"lineNumber":279,"utf16Col":0},"end":{"lineNumber":279,"utf16Col":32}}},{"name":"ticket_dict","kind":"constant","identStart":8585,"identEnd":8596,"extentStart":8585,"extentEnd":8601,"fullyQualifiedName":"ticket_dict","identUtf16":{"start":{"lineNumber":280,"utf16Col":0},"end":{"lineNumber":280,"utf16Col":11}},"extentUtf16":{"start":{"lineNumber":280,"utf16Col":0},"end":{"lineNumber":280,"utf16Col":16}}},{"name":"load","kind":"function","identStart":8609,"identEnd":8613,"extentStart":8605,"extentEnd":8771,"fullyQualifiedName":"load","identUtf16":{"start":{"lineNumber":282,"utf16Col":4},"end":{"lineNumber":282,"utf16Col":8}},"extentUtf16":{"start":{"lineNumber":282,"utf16Col":0},"end":{"lineNumber":287,"utf16Col":30}}},{"name":"s","kind":"function","identStart":8783,"identEnd":8784,"extentStart":8779,"extentEnd":8901,"fullyQualifiedName":"s","identUtf16":{"start":{"lineNumber":291,"utf16Col":4},"end":{"lineNumber":291,"utf16Col":5}},"extentUtf16":{"start":{"lineNumber":291,"utf16Col":0},"end":{"lineNumber":295,"utf16Col":28}}},{"name":"menu","kind":"function","identStart":9055,"identEnd":9059,"extentStart":9051,"extentEnd":9541,"fullyQualifiedName":"menu","identUtf16":{"start":{"lineNumber":305,"utf16Col":4},"end":{"lineNumber":305,"utf16Col":8}},"extentUtf16":{"start":{"lineNumber":305,"utf16Col":0},"end":{"lineNumber":317,"utf16Col":15}}}]}},"csrf_tokens":{"/PowerstarPrasad/projects_5/branches":{"post":"lQDcOwczXljEn2MAvYy9x38qvB3G_Kt17kEimjLDBvmKxNJ8FYtdxZvmTQn4pKIstaEXbz-58ZTT2BSYKFcF6g"}}},"title":"projects_5/railway project.py at main · PowerstarPrasad/projects_5","locale":"en","appPayload":{"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-848bb9a5da17.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-f47a66bce6ac.js","githubDevUrl":"https://github.dev/","enabled_features":{"virtualize_file_tree":true,"react_repos_overview":false,"repos_new_shortcut_enabled":true,"blob_navigation_cursor":true,"code_nav_ui_events":false,"ref_selector_v2":false,"codeview_codemirror_next":true,"blob_firefox_separate_characters":false,"copilot_conversational_ux":false}}}</script>
  <div data-target="react-app.reactRoot"><div color="fg.default" font-family="normal" data-portal-root="true" class="BaseStyles__Base-sc-nfjs56-0 bmmbtJ"><div id="__primerPortalRoot__" style="z-index: 10; position: absolute; width: 100%;"></div><meta data-hydrostats="publish">    <button hidden="" data-testid="header-permalink-button" data-hotkey="y,Y" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="y,Y"></button><div class="Box-sc-g0xbh4-0"><div class="Box-sc-g0xbh4-0 fSWWem" style="--sticky-pane-height: calc(100vh - (max(104px, 0px)));"><div class="Box-sc-g0xbh4-0 kPPmzM"><div class="Box-sc-g0xbh4-0 cIAPDV"><div tabindex="0" class="Box-sc-g0xbh4-0 gvCnwW"><div class="Box-sc-g0xbh4-0 ioxSsX"><div class="Box-sc-g0xbh4-0 eUyHuk"></div><div class="Box-sc-g0xbh4-0 cvKirU"><div role="separator" class="Box-sc-g0xbh4-0 dZCkhR"></div></div><div class="Box-sc-g0xbh4-0 gNdDUH" style="--pane-width: 320px;"><span class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 rTZSs"><form><label for=":r2e:-width-input">Pane width</label><p id=":r2e:-input-hint">Use a value between 17% and 38%</p><input id=":r2e:-width-input" aria-describedby=":r2e:-input-hint" name="pane-width" inputmode="numeric" pattern="[0-9]*" autocorrect="off" autocomplete="off" type="text" value="21" fdprocessedid="oa7m5d"><button type="submit" fdprocessedid="0fb23n">Change width</button></form></span><div id="repos-file-tree" class="Box-sc-g0xbh4-0 dkMzXD"><div class="Box-sc-g0xbh4-0 hBSSUC"><div class="Box-sc-g0xbh4-0 iPurHz"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 fNPcqd"><button data-component="IconButton" data-testid="collapse-file-tree-button" aria-label="Side panel" aria-expanded="true" aria-controls="repos-file-tree" data-hotkey="Control+b" class="types__StyledButton-sc-ws60qy-0 hNyQml" data-no-visuals="true" fdprocessedid="7ogrol"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-sidebar-expand" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="m4.177 7.823 2.396-2.396A.25.25 0 0 1 7 5.604v4.792a.25.25 0 0 1-.427.177L4.177 8.177a.25.25 0 0 1 0-.354Z"></path><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25H9.5v-13Zm12.5 13a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11v13Z"></path></svg></button><button hidden="" data-testid="" data-hotkey="Control+b" data-hotkey-scope="read-only-cursor-text-area"></button></h2><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 imcwCi">Code</h2></div><div class="Box-sc-g0xbh4-0 hVHHYa"><div class="Box-sc-g0xbh4-0 idZfsJ"><button type="button" id="branch-picker-1687271955492" aria-haspopup="true" tabindex="0" data-hotkey="w" aria-label="main branch" data-testid="anchor-button" class="types__StyledButton-sc-ws60qy-0 cZRqXf react-repos-tree-pane-ref-selector width-full ref-selector-class" fdprocessedid="a866gl"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text"><div class="Box-sc-g0xbh4-0 cFPoqW"><div class="Box-sc-g0xbh4-0 bwTunw"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="Box-sc-g0xbh4-0 caeYDk"><span class="Text-sc-17v1xeu-0 bOMzPg">&nbsp;main</span></div></div></span><span data-component="trailingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-hotkey="w" data-hotkey-scope="read-only-cursor-text-area"></button></div><span role="tooltip" aria-label="Add file" class="Tooltip__TooltipBase-sc-uha8qm-0 fCnxTL tooltipped-s"><a sx="[object Object]" data-component="IconButton" aria-label="Add file" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 gTeenv" href="https://github.com/PowerstarPrasad/projects_5/new/main"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-plus" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg></a></span><button data-component="IconButton" aria-label="Search this repository" data-hotkey="/" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 VplrY" fdprocessedid="rjm8c3"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></button><button hidden="" data-testid="" data-hotkey="/" data-hotkey-scope="read-only-cursor-text-area"></button></div></div><div class="Box-sc-g0xbh4-0 jRttMj"><button hidden="" data-testid="" data-hotkey="t,T" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="t,T"></button><span class="_TextInputWrapper__TextInputBaseWrapper-sc-apywy2-0 _TextInputWrapper__TextInputWrapper-sc-apywy2-1 bqFowW jhluSD TextInput-wrapper" aria-live="polite" aria-busy="false"><span class="TextInput-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><input type="text" aria-label="Go to file" role="combobox" aria-controls="file-results-list" aria-expanded="false" aria-haspopup="dialog" autocorrect="off" spellcheck="false" placeholder="Go to file" data-component="input" class="_UnstyledTextInput__UnstyledTextInput-sc-31b2um-0 dFGJZq" value="" fdprocessedid="y7nlah"><span class="TextInput-icon"><div class="Box-sc-g0xbh4-0 cNvKlH"><kbd>t</kbd></div></span></span></div><div class="Box-sc-g0xbh4-0 bYLCoz"><div><div data-testid="repos-file-tree-container" class="Box-sc-g0xbh4-0 hJcmjJ"><nav aria-label="File Tree Navigation"><span role="status" aria-live="polite" aria-atomic="true" class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 rTZSs"></span><ul role="tree" aria-label="Files" class="TreeView__UlBox-sc-4ex6b6-0 hLwWNO"><li class="PRIVATE_TreeView-item" tabindex="0" id="LordTiru_Bank-Project.py-item" role="treeitem" aria-labelledby=":r2k:" aria-describedby=":r2l: :r2m:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer / spacer / spacer / spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r2k:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":r2l:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>LordTiru_Bank-Project.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="README.md-item" role="treeitem" aria-labelledby=":r2n:" aria-describedby=":r2o: :r2p:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer / spacer / spacer / spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r2n:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":r2o:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>README.md</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="railway project.py-item" role="treeitem" aria-labelledby=":r2q:" aria-describedby=":r2r: :r2s:" aria-level="1" aria-current="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level: 1;"><div style="grid-area: spacer / spacer / spacer / spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r2q:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":r2r:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>railway project.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="super-market project.py-item" role="treeitem" aria-labelledby=":r2t:" aria-describedby=":r2u: :r2v:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer / spacer / spacer / spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r2t:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":r2u:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>super-market project.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="titanic_project.ipynb-item" role="treeitem" aria-labelledby=":r30:" aria-describedby=":r31: :r32:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer / spacer / spacer / spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r30:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":r31:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>titanic_project.ipynb</span></span></div></div></li></ul></nav></div></div><div class="Box-sc-g0xbh4-0 hwhShM"><div class="Box-sc-g0xbh4-0 cYPxpP"><a href="https://docs.github.com/en/repositories/working-with-files/using-files/navigating-code-on-github" target="_blank" class="Link__StyledLink-sc-14289xe-0 bJBoUI">Documentation</a>&nbsp;•&nbsp;<a href="https://github.com/orgs/community/discussions/54546" target="_blank" class="Link__StyledLink-sc-14289xe-0 bJBoUI">Share feedback</a></div></div></div><div class="Box-sc-g0xbh4-0 fBtiVT"><div class="Box-sc-g0xbh4-0 cYPxpP"><a href="https://docs.github.com/en/repositories/working-with-files/using-files/navigating-code-on-github" target="_blank" class="Link__StyledLink-sc-14289xe-0 bJBoUI">Documentation</a>&nbsp;•&nbsp;<a href="https://github.com/orgs/community/discussions/54546" target="_blank" class="Link__StyledLink-sc-14289xe-0 bJBoUI">Share feedback</a></div></div></div></div></div></div><main class="Box-sc-g0xbh4-0 emFMJu"><div class="Box-sc-g0xbh4-0"></div><div class="Box-sc-g0xbh4-0 hlUAHL"><div data-selector="repos-split-pane-content" tabindex="0" class="Box-sc-g0xbh4-0 iStsmI"><div class="Box-sc-g0xbh4-0 SXuuD"><div id="StickyHeader" class="Box-sc-g0xbh4-0 bDwCYs"><div class="Box-sc-g0xbh4-0 rmFvl"><div class="Box-sc-g0xbh4-0 dyczTK"><div class="Box-sc-g0xbh4-0 jJaodr"><div class="Box-sc-g0xbh4-0 eTvGbF"><nav data-testid="breadcrumbs" aria-labelledby="breadcrumb-heading" id="breadcrumb" class="Box-sc-g0xbh4-0 kzRgrI"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading" id="breadcrumb-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 cmAPIB"><li class="Box-sc-g0xbh4-0 jwXCBK"><a sx="[object Object]" data-testid="breadcrumbs-repo-link" class="Link__StyledLink-sc-14289xe-0 iJtJJh" href="https://github.com/PowerstarPrasad/projects_5/tree/main">projects_5</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 fWVgeN">/</span><h1 tabindex="-1" id="file-name-id" class="Heading__StyledHeading-sc-1c1dgg0-0 diwsLq">railway project.py</h1></div><button data-component="IconButton" aria-label="Copy path" data-testid="breadcrumb-copy-path-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 dsNAFH" fdprocessedid="mlonv7"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div></div><div class="Box-sc-g0xbh4-0 gtBUEp"><div class="d-flex gap-2"></div></div></div></div></div></div><div class="Box-sc-g0xbh4-0 bhAUGf"></div><div class="Box-sc-g0xbh4-0 fwKaNR"><div class="Box-sc-g0xbh4-0 gxnDme"><div class="Box-sc-g0xbh4-0 fZUFsx"><div class="Box-sc-g0xbh4-0 jnbeuA"><div class="Box-sc-g0xbh4-0 eTvGbF"><nav data-testid="breadcrumbs" aria-labelledby="file-name-editor-breadcrumb-heading" id="file-name-editor-breadcrumb" class="Box-sc-g0xbh4-0 kzRgrI"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading" id="file-name-editor-breadcrumb-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 cmAPIB"><li class="Box-sc-g0xbh4-0 jwXCBK"><a sx="[object Object]" data-testid="breadcrumbs-repo-link" class="Link__StyledLink-sc-14289xe-0 iJtJJh" href="https://github.com/PowerstarPrasad/projects_5/tree/main">projects_5</a></li></ol></nav></div><div class="Box-sc-g0xbh4-0 lhFvfi"><span aria-hidden="true" class="Text-sc-17v1xeu-0 fWVgeN">/</span><span class="_TextInputWrapper__TextInputBaseWrapper-sc-apywy2-0 _TextInputWrapper__TextInputWrapper-sc-apywy2-1 gFWVxl WAoMk TextInput-wrapper" aria-live="polite" aria-busy="false"><input type="text" aria-label="File name" aria-describedby="file-name-editor-breadcrumb" placeholder="Name your file..." data-component="input" class="_UnstyledTextInput__UnstyledTextInput-sc-31b2um-0 dFGJZq" value="railway project.py" fdprocessedid="9tmf9k"></span><div class="Box-sc-g0xbh4-0 dGzNKP">in</div><div class="Box-sc-g0xbh4-0"><a href="https://github.com/PowerstarPrasad/projects_5/tree/main" class="BranchName-sc-sg8jsy-0 iVNDSi">main</a></div></div></div></div><div class="Box-sc-g0xbh4-0 cnECWi"><a sx="[object Object]" type="button" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 hgSees" href="https://github.com/PowerstarPrasad/projects_5/blob/main/railway%20project.py"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Cancel changes</span></span></a><button type="button" data-hotkey="Meta+s,Control+s" disabled="" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 dodsdL"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Commit changes...</span></span></button></div></div><div class="Box-sc-g0xbh4-0 cpPHtE"><div class="Box-sc-g0xbh4-0 ktGGEf"><div class="Box-sc-g0xbh4-0 gkfBtX"><div class="Box-sc-g0xbh4-0 gQjvB"><ul aria-label="Edit mode" class="SegmentedControl__SegmentedControlList-sc-1rzig82-0 bELcLY"><li class="Box-sc-g0xbh4-0 fXBLEV"><button aria-current="true" class="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0 eNSiNz" fdprocessedid="7jh7vr"><span class="segmentedControl-content"><div class="Box-sc-g0xbh4-0 segmentedControl-text">Edit</div></span></button></li><li class="Box-sc-g0xbh4-0 gbKtit"><button aria-current="false" class="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0 cuqBaK" fdprocessedid="6a6zmo"><span class="segmentedControl-content"><div class="Box-sc-g0xbh4-0 segmentedControl-text">Preview</div></span></button></li></ul><div class="Box-sc-g0xbh4-0 bAIjlC"></div><div class="Box-sc-g0xbh4-0 ikKSSu"></div><div class="Box-sc-g0xbh4-0 hrJmOP"><div class="Box-sc-g0xbh4-0 hShodj"><div display="flex" class="Box-sc-g0xbh4-0 eVfmLP"><label for="react-aria-1" class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 rTZSs">Indent mode</label><span class="_TextInputWrapper__TextInputBaseWrapper-sc-apywy2-0 _TextInputWrapper__TextInputWrapper-sc-apywy2-1 kuqoFO fGOtuD"><select aria-invalid="false" data-hasplaceholder="false" aria-label="Indent mode" id="react-aria-1" aria-describedby="" class="Select__StyledSelect-sc-li6bhs-0 siQqA" fdprocessedid="300nvr"><optgroup label="Indent mode"><option value="spaces">Spaces</option><option value="tab">Tabs</option></optgroup></select><svg width="16" height="16" fill="currentColor" xmlns="http://www.w3.org/2000/svg" class="Select__ArrowIndicator-sc-li6bhs-1 cmdteN"><path d="m4.074 9.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.043 9H4.251a.25.25 0 0 0-.177.427ZM4.074 7.47 7.47 4.073a.25.25 0 0 1 .354 0L11.22 7.47a.25.25 0 0 1-.177.426H4.251a.25.25 0 0 1-.177-.426Z"></path></svg></span></div><div display="flex" class="Box-sc-g0xbh4-0 eVfmLP"><label for="react-aria-2" class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 rTZSs">Indent size</label><span class="_TextInputWrapper__TextInputBaseWrapper-sc-apywy2-0 _TextInputWrapper__TextInputWrapper-sc-apywy2-1 kuqoFO fGOtuD"><select aria-invalid="false" data-hasplaceholder="false" aria-label="Indent size" id="react-aria-2" aria-describedby="" class="Select__StyledSelect-sc-li6bhs-0 siQqA" fdprocessedid="augd3w"><optgroup label="Indent size"><option value="2">2</option><option value="4">4</option><option value="8">8</option></optgroup></select><svg width="16" height="16" fill="currentColor" xmlns="http://www.w3.org/2000/svg" class="Select__ArrowIndicator-sc-li6bhs-1 cmdteN"><path d="m4.074 9.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.043 9H4.251a.25.25 0 0 0-.177.427ZM4.074 7.47 7.47 4.073a.25.25 0 0 1 .354 0L11.22 7.47a.25.25 0 0 1-.177.426H4.251a.25.25 0 0 1-.177-.426Z"></path></svg></span></div><div display="flex" class="Box-sc-g0xbh4-0 eVfmLP"><label for="react-aria-3" class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 rTZSs">Line wrap mode</label><span class="_TextInputWrapper__TextInputBaseWrapper-sc-apywy2-0 _TextInputWrapper__TextInputWrapper-sc-apywy2-1 kuqoFO fGOtuD"><select aria-invalid="false" data-hasplaceholder="false" aria-label="Line wrap mode" id="react-aria-3" aria-describedby="" class="Select__StyledSelect-sc-li6bhs-0 siQqA" fdprocessedid="m43lb2"><optgroup label="Line wrap mode"><option value="off">No wrap</option><option value="on">Soft wrap</option></optgroup></select><svg width="16" height="16" fill="currentColor" xmlns="http://www.w3.org/2000/svg" class="Select__ArrowIndicator-sc-li6bhs-1 cmdteN"><path d="m4.074 9.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.043 9H4.251a.25.25 0 0 0-.177.427ZM4.074 7.47 7.47 4.073a.25.25 0 0 1 .354 0L11.22 7.47a.25.25 0 0 1-.177.426H4.251a.25.25 0 0 1-.177-.426Z"></path></svg></span></div></div></div></div></div><div class="Box-sc-g0xbh4-0 ccyNBX react-code-view-edit"><div><div class="cm-editor ͼ1 ͼ2 ͼk ͼ5 js-codemirror-editor" data-hpc="true" data-testid="codemirror-editor"><div aria-live="polite" style="position: fixed; top: -10000px;"></div><div tabindex="-1" class="cm-scroller"><div class="cm-gutters" aria-hidden="true" style="min-height: 6472px; position: sticky;"><div class="cm-gutter cm-lineNumbers"><div class="cm-gutterElement" style="height: 0px; visibility: hidden; pointer-events: none;">999</div><div class="cm-gutterElement" style="height: 20px; margin-top: 8px;">1</div><div class="cm-gutterElement" style="height: 20px;">2</div><div class="cm-gutterElement" style="height: 20px;">3</div><div class="cm-gutterElement" style="height: 20px;">4</div><div class="cm-gutterElement" style="height: 20px;">5</div><div class="cm-gutterElement" style="height: 20px;">6</div><div class="cm-gutterElement" style="height: 20px;">7</div><div class="cm-gutterElement" style="height: 20px;">8</div><div class="cm-gutterElement" style="height: 20px;">9</div><div class="cm-gutterElement" style="height: 20px;">10</div><div class="cm-gutterElement" style="height: 20px;">11</div><div class="cm-gutterElement" style="height: 20px;">12</div><div class="cm-gutterElement" style="height: 20px;">13</div><div class="cm-gutterElement" style="height: 20px;">14</div><div class="cm-gutterElement" style="height: 20px;">15</div><div class="cm-gutterElement" style="height: 20px;">16</div><div class="cm-gutterElement" style="height: 20px;">17</div><div class="cm-gutterElement" style="height: 20px;">18</div><div class="cm-gutterElement" style="height: 20px;">19</div><div class="cm-gutterElement" style="height: 20px;">20</div><div class="cm-gutterElement" style="height: 20px;">21</div><div class="cm-gutterElement" style="height: 20px;">22</div><div class="cm-gutterElement" style="height: 20px;">23</div><div class="cm-gutterElement" style="height: 20px;">24</div><div class="cm-gutterElement" style="height: 20px;">25</div><div class="cm-gutterElement" style="height: 20px;">26</div><div class="cm-gutterElement" style="height: 20px;">27</div><div class="cm-gutterElement" style="height: 20px;">28</div><div class="cm-gutterElement" style="height: 20px;">29</div><div class="cm-gutterElement" style="height: 20px;">30</div><div class="cm-gutterElement" style="height: 20px;">31</div><div class="cm-gutterElement" style="height: 20px;">32</div><div class="cm-gutterElement" style="height: 20px;">33</div><div class="cm-gutterElement" style="height: 20px;">34</div><div class="cm-gutterElement" style="height: 20px;">35</div><div class="cm-gutterElement" style="height: 20px;">36</div><div class="cm-gutterElement" style="height: 20px;">37</div><div class="cm-gutterElement" style="height: 20px;">38</div><div class="cm-gutterElement" style="height: 20px;">39</div><div class="cm-gutterElement" style="height: 20px;">40</div><div class="cm-gutterElement" style="height: 20px;">41</div><div class="cm-gutterElement" style="height: 20px;">42</div><div class="cm-gutterElement" style="height: 20px;">43</div><div class="cm-gutterElement" style="height: 20px;">44</div><div class="cm-gutterElement" style="height: 20px;">45</div><div class="cm-gutterElement" style="height: 20px;">46</div><div class="cm-gutterElement" style="height: 20px;">47</div><div class="cm-gutterElement" style="height: 20px;">48</div><div class="cm-gutterElement" style="height: 20px;">49</div><div class="cm-gutterElement" style="height: 20px;">50</div><div class="cm-gutterElement" style="height: 20px;">51</div><div class="cm-gutterElement" style="height: 20px;">52</div><div class="cm-gutterElement" style="height: 20px;">53</div><div class="cm-gutterElement" style="height: 20px;">54</div><div class="cm-gutterElement" style="height: 20px;">55</div><div class="cm-gutterElement" style="height: 20px;">56</div><div class="cm-gutterElement" style="height: 20px;">57</div><div class="cm-gutterElement" style="height: 20px;">58</div><div class="cm-gutterElement" style="height: 20px;">59</div><div class="cm-gutterElement" style="height: 20px;">60</div><div class="cm-gutterElement" style="height: 20px;">61</div><div class="cm-gutterElement" style="height: 20px;">62</div></div></div><div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" style="tab-size: 8; flex-basis: 1509px;" role="textbox" aria-multiline="true" aria-label="Editing railway project.py file contents" aria-describedby="focus-trap-help-panel" data-language="python"><div class="cm-line"><span class="ͼ6">import</span> random</div><div class="cm-line"><span class="ͼ6">import</span> pickle</div><div class="cm-line"><span class="ͼ6">import</span> sys</div><div class="cm-line"><br></div><div class="cm-line">logged_in = <span class="ͼb">False</span></div><div class="cm-line">uid = <span class="ͼb">0</span></div><div class="cm-line">pwd = <span class="ͼ9">''</span></div><div class="cm-line"><br></div><div class="cm-line"><span class="ͼ6">class</span> train:</div><div class="cm-line">    <span class="ͼ6">def</span> <span class="ͼd">__init__</span><span class="ͼ8">(</span>self,name = <span class="ͼ9">''</span>, num = <span class="ͼb">0</span>, arr_time = <span class="ͼ9">''</span>,dep_time = <span class="ͼ9">''</span>,src = <span class="ͼ9">''</span> ,des = <span class="ͼ9">''</span>,day_of_travel = <span class="ͼ9">''</span>,seat_available_in_1AC = <span class="ͼb">0</span>,seat_available_in_2AC = <span class="ͼb">0</span>,seat_available_in_SL = <span class="ͼb">0</span>,fare_1ac = <span class="ͼb">0</span>, fare_2ac = <span class="ͼb">0</span> ,fare_sl = <span class="ͼb">0</span><span class="ͼ8">)</span>:</div><div class="cm-line">        self.<span class="ͼa">name</span> = name</div><div class="cm-line">        self.<span class="ͼa">num</span> = num</div><div class="cm-line">        self.<span class="ͼa">arr_time</span> = arr_time</div><div class="cm-line">        self.<span class="ͼa">dep_time</span> = dep_time</div><div class="cm-line">        self.<span class="ͼa">src</span> = src</div><div class="cm-line">        self.<span class="ͼa">des</span> = des</div><div class="cm-line">        self.<span class="ͼa">day_of_travel</span> = day_of_travel</div><div class="cm-line">        self.<span class="ͼa">seats</span> = <span class="ͼ8">{</span><span class="ͼ9">'1AC'</span> : seat_available_in_1AC, <span class="ͼ9">'2AC'</span>: seat_available_in_2AC,<span class="ͼ9">'SL'</span>: seat_available_in_SL<span class="ͼ8">}</span></div><div class="cm-line">        self.<span class="ͼa">fare</span> = <span class="ͼ8">{</span><span class="ͼ9">'1AC'</span> : fare_1ac,<span class="ͼ9">'2AC'</span> : fare_2ac ,<span class="ͼ9">'SL'</span> : fare_sl<span class="ͼ8">}</span></div><div class="cm-line">    <span class="ͼ6">def</span> <span class="ͼd">print_seat_availablity</span><span class="ͼ8">(</span>self<span class="ͼ8">)</span>:</div><div class="cm-line">    	<span class="ͼc">print</span><span class="ͼ8">(</span><span class="ͼ9">"No. of seats available in 1AC :- "</span>+<span class="ͼc">str</span><span class="ͼ8">(</span>self.<span class="ͼa">seats</span><span class="ͼ8">[</span><span class="ͼ9">'1AC'</span><span class="ͼ8">]</span><span class="ͼ8">)</span><span class="ͼ8">)</span></div><div class="cm-line">    	<span class="ͼc">print</span><span class="ͼ8">(</span><span class="ͼ9">"No. of seats available in 2AC :- "</span>+<span class="ͼc">str</span><span class="ͼ8">(</span>self.<span class="ͼa">seats</span><span class="ͼ8">[</span><span class="ͼ9">'2AC'</span><span class="ͼ8">]</span><span class="ͼ8">)</span><span class="ͼ8">)</span></div><div class="cm-line">    	<span class="ͼc">print</span><span class="ͼ8">(</span><span class="ͼ9">"No. of seats available in SL :- "</span>+<span class="ͼc">str</span><span class="ͼ8">(</span>self.<span class="ͼa">seats</span><span class="ͼ8">[</span><span class="ͼ9">'SL'</span><span class="ͼ8">]</span><span class="ͼ8">)</span><span class="ͼ8">)</span></div><div class="cm-line">    <span class="ͼ6">def</span> <span class="ͼd">check_availabilty</span><span class="ͼ8">(</span>self,coach=<span class="ͼ9">''</span>,ticket_num = <span class="ͼb">0</span><span class="ͼ8">)</span>:</div><div class="cm-line">    	coach = coach.<span class="ͼa">upper</span><span class="ͼ8">(</span><span class="ͼ8">)</span></div><div class="cm-line">    	<span class="ͼ6">if</span> coach <span class="ͼ6">not</span> <span class="ͼ6">in</span> <span class="ͼ8">(</span><span class="ͼ9">'SL'</span>,<span class="ͼ9">'1AC'</span>,<span class="ͼ9">'2AC'</span><span class="ͼ8">)</span>:</div><div class="cm-line">    		<span class="ͼc">print_seat_availablity</span><span class="ͼ8">(</span><span class="ͼ8">)</span></div><div class="cm-line">    		coach = <span class="ͼc">input</span><span class="ͼ8">(</span><span class="ͼ9">"Enter the coach(1AC/2AC/SL) :-"</span><span class="ͼ8">)</span></div><div class="cm-line">    	<span class="ͼ6">else</span>:</div><div class="cm-line">    		<span class="ͼ6">if</span> self.<span class="ͼa">seats</span><span class="ͼ8">[</span>coach<span class="ͼ8">]</span> == <span class="ͼb">0</span>:</div><div class="cm-line">    			<span class="ͼ6">return</span> <span class="ͼb">False</span></div><div class="cm-line">    		<span class="ͼ6">elif</span> self.<span class="ͼa">seats</span><span class="ͼ8">[</span>coach<span class="ͼ8">]</span> &gt;= ticket_num:</div><div class="cm-line">    			<span class="ͼ6">return</span> <span class="ͼb">True</span></div><div class="cm-line">    		<span class="ͼ6">else</span>:</div><div class="cm-line">    			<span class="ͼ6">return</span> <span class="ͼb">False</span></div><div class="cm-line">    <span class="ͼ6">def</span> <span class="ͼd">book_ticket</span><span class="ͼ8">(</span>self,coach = <span class="ͼ9">''</span>,no_of_tickets = <span class="ͼb">0</span><span class="ͼ8">)</span>:</div><div class="cm-line">    	self.<span class="ͼa">seats</span><span class="ͼ8">[</span>coach<span class="ͼ8">]</span> -= no_of_tickets</div><div class="cm-line">    	<span class="ͼ6">return</span> <span class="ͼb">True</span></div><div class="cm-line"><br></div><div class="cm-line"><br></div><div class="cm-line"><span class="ͼ6">class</span> ticket:</div><div class="cm-line">	<span class="ͼ6">def</span> <span class="ͼd">__init__</span><span class="ͼ8">(</span>self,train,user,ticket_num,coach<span class="ͼ8">)</span>:</div><div class="cm-line">		self.<span class="ͼa">pnr</span> = <span class="ͼc">str</span><span class="ͼ8">(</span>train.<span class="ͼa">num</span><span class="ͼ8">)</span>+<span class="ͼc">str</span><span class="ͼ8">(</span>user.<span class="ͼa">uid</span><span class="ͼ8">)</span>+<span class="ͼc">str</span><span class="ͼ8">(</span>random.<span class="ͼa">randint</span><span class="ͼ8">(</span><span class="ͼb">100</span>,<span class="ͼb">999</span><span class="ͼ8">)</span><span class="ͼ8">)</span></div><div class="cm-line">		self.<span class="ͼa">train_num</span> = train.<span class="ͼa">num</span></div><div class="cm-line">		self.<span class="ͼa">coach</span> = coach</div><div class="cm-line">		self.<span class="ͼa">uid</span> = user.<span class="ͼa">uid</span></div><div class="cm-line">		self.<span class="ͼa">train_name</span> = train.<span class="ͼa">name</span></div><div class="cm-line">		self.<span class="ͼa">user_name</span> = user.<span class="ͼa">name</span></div><div class="cm-line">		self.<span class="ͼa">ticket_num</span> = ticket_num</div><div class="cm-line">		user.<span class="ͼa">history</span>.<span class="ͼa">update</span><span class="ͼ8">(</span><span class="ͼ8">{</span>self.<span class="ͼa">pnr</span> : self<span class="ͼ8">}</span><span class="ͼ8">)</span></div><div class="cm-line">		ticket_dict.<span class="ͼa">update</span><span class="ͼ8">(</span><span class="ͼ8">{</span>self.<span class="ͼa">pnr</span> : self<span class="ͼ8">}</span><span class="ͼ8">)</span></div><div class="cm-line"><br></div><div class="cm-line"><br></div><div class="cm-line"><br></div><div class="cm-line"><span class="ͼ6">class</span> user:</div><div class="cm-line">	<span class="ͼ6">def</span> <span class="ͼd">__init__</span><span class="ͼ8">(</span>self,uid = <span class="ͼb">0</span>,name = <span class="ͼ9">''</span>,hometown = <span class="ͼ9">''</span>,cell_num = <span class="ͼ9">''</span>,pwd = <span class="ͼ9">''</span><span class="ͼ8">)</span>:</div><div class="cm-line">		self.<span class="ͼa">uid</span> = uid</div><div class="cm-line">		self.<span class="ͼa">name</span> = name</div><div class="cm-line">		self.<span class="ͼa">hometown</span> = <span class="ͼ9">''</span></div><div class="cm-line">		self.<span class="ͼa">cell_num</span> = <span class="ͼ9">''</span></div><div class="cm-line">		self.<span class="ͼa">pwd</span> = pwd</div><div class="cm-line">		self.<span class="ͼa">history</span> = <span class="ͼ8">{</span><span class="ͼ8">}</span></div><div contenteditable="false" style="height: 5220px;"></div></div></div><div class="cm-panels cm-panels-bottom" style="bottom: 0px;"><div class="cm-help-panel cm-panel" id="focus-trap-help-panel">Use <kbd>Control + Shift + m</kbd> to toggle the <kbd>tab</kbd> key moving focus. Alternatively, use <kbd>esc</kbd> then <kbd>tab</kbd> to move to the next interactive element on the page.</div></div></div></div></div></div></div></div></div></div><div class="Box-sc-g0xbh4-0"></div></main></div></div></div><div id="find-result-marks-container" class="Box-sc-g0xbh4-0 aZrVR"></div><button hidden="" data-testid="" data-hotkey="Control+F6,Control+Shift+F6" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Control+F6,Control+Shift+F6"></button></div>    </div><script type="application/json" id="__PRIMER_DATA__">{"resolvedServerColorMode":"night"}</script></div>
</react-app>




  </div>

</turbo-frame>

    </main>
  </div>

  </div>

          <footer class="footer width-full container-xl p-responsive" role="contentinfo" hidden="">
  <h2 class="sr-only">Footer</h2>

  <div class="position-relative d-flex flex-items-center pb-2 f6 color-fg-muted color-border-muted flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap mt-0 pt-6">
    <div class="list-style-none d-flex flex-wrap col-0 col-lg-2 flex-justify-start flex-lg-justify-between mb-2 mb-lg-0">
      <div class="mt-2 mt-lg-0 d-flex flex-items-center">
        <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-2" href="https://github.com/">
          <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
</a>        <span>
        © 2023 GitHub, Inc.
        </span>
      </div>
    </div>

    <nav aria-label="Footer" class="col-12 col-lg-8">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>
      <ul class="list-style-none d-flex flex-wrap col-12 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">
          <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}">Terms</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}">Privacy</a></li>
          <li class="mr-3 mr-lg-0"><a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security">Security</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://www.githubstatus.com/" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}">Status</a></li>
          <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to help, text:Docs" href="https://docs.github.com/">Docs</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://support.github.com/?tags=dotcom-footer" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}">Contact GitHub</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Pricing&quot;,&quot;label&quot;:&quot;text:Pricing&quot;}">Pricing</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to api&quot;,&quot;label&quot;:&quot;text:api&quot;}">API</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://services.github.com/" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to training&quot;,&quot;label&quot;:&quot;text:training&quot;}">Training</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://github.blog/" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to blog&quot;,&quot;label&quot;:&quot;text:blog&quot;}">Blog</a></li>
          <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>
      </ul>
    </nav>
  </div>

  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 color-fg-muted"></span>
  </div>
</footer>




  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>
<template id="snippet-clipboard-copy-button-unpositioned"></template>


    <style>
      .user-mention[href$="/PowerstarPrasad"] {
        color: var(--color-user-mention-fg);
        background-color: var(--color-user-mention-bg);
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
        padding: 0 2px;
      }
    </style>


    </div>

    <div id="js-global-screen-reader-notice" class="sr-only" aria-live="polite">Editing projects_5/railway project.py at main · PowerstarPrasad/projects_5 · GitHub</div>
  


</body></html>