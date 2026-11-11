# 関数・アドレス事典

> 迫真戦記 ver0.67 の研究用辞書です。静的解析・既存研究報告の情報であり、すべて実機確認済みではありません。
> 原作EXE、非公開の研究原本、Git履歴は収録していません。

収録：アドレス **516項目**（関数 **373件**）、構造体フィールド **122件**、直接CALL **2373レコード**。

## 関数・アドレス一覧

| VA | 種別 | 名称 | 概要 |
|---|---|---|---|
| [0x00402C40](symbols/00402C40.md) | func | UnitData_CompareRawStringKeys | UnitData のキー比較で呼び出す生バイトの文字列比較。共通先頭が一致しても長さが異なれば別キーとなる。 |
| [0x00406E20](symbols/00406E20.md) | func | Nop_406E20 | 何もしない関数（TempStatusWnd の vtable +0x44） |
| [0x0040D0A0](symbols/0040D0A0.md) | func | BattleStatusWnd_Open | 戦況ウィンドウを開く処理 |
| [0x0040E220](symbols/0040E220.md) | func | SimpleBattle_CommitResult | 簡易戦闘の毎フレーム処理（BattleWnd 副vtable+4、this=W+0x28）。VM が動いていれば 0x4338D0、そうでなければ 0x40E27F で 0x40E2F0 を呼び、0 以外なら 0x40E2B9 で 0x493630(…, ret==1) → 0x40F000 → 0x48ABF0。戻り値 1＝攻撃側の勝ち、外部結果の反映、0 を返し続けての待機を実機確認 |
| [0x0040E27F](symbols/0040E27F.md) | code | SimpleBattle_SimCallSite | 簡易戦闘の毎フレームの計算呼出し call 0x40E2F0（EAX=戦況ウィンドウ W、戻り値 0=続行/1=攻撃側の勝ち/2=防衛側の勝ち）。直接呼出しはここだけ。戦闘差し替えの差し替え口。0 を返し続けても原作は戦況ウィンドウのまま待つ（実機） |
| [0x0040E2F0](symbols/0040E2F0.md) | func | SimpleBattle_RunBoundedRounds | 簡略戦闘の反復処理。局所カウンタの上限は500で、上限到達時の戻り値0は勝敗確定を意味しない。 |
| [0x0040ED80](symbols/0040ED80.md) | func | Rng_RangeInclusive | lo + ftol(rand/32768*(hi-lo))。rand を 1 回使う |
| [0x0040F000](symbols/0040F000.md) | func | SimpleBattle_ReleaseSides | 簡略戦闘の結果反映後に両陣営の virtual +0x10 を呼び、戦闘用ユニットを破棄する処理へ進む。 |
| [0x0040F320](symbols/0040F320.md) | func | SimpleBattle_BuildUnitRoster | 簡略戦闘用 SimpleUnit を生成し、更新対象の配列へ登録する経路を含む。 |
| [0x004154F0](symbols/004154F0.md) | func | VecString_Clear | vector&lt;std::string&gt; の中身を壊して領域を返し、3 つのポインタを 0 にする（ECX=vector）。 内部契約は著者STATIC記述、実機区分は試験での使用成功に限定。 |
| [0x00415530](symbols/00415530.md) | func | VecString_PushBack | vector&lt;std::string&gt;::push_back。独自の呼び方: ECX=追加する std::string、EDI=vector。原作の確保関数で写す。setv/addv が配列変数を作るときに使う。 内部契約は著者STATIC記述、実機区分は試験での使用成功に限定。 |
| [0x00415CF0](symbols/00415CF0.md) | func | Tree_EraseIteratorRange | Original x86 bounded 182B code compares range endpoints, calls 0x416870 for full-tree range and 0x416220 per-node on partial range; iterator ABI, key ownership and gameplay effect VERIFY |
| [0x00416220](symbols/00416220.md) | func | Tree_EraseRangePartialNode | Original x86 partial-range tree-node erase: invalid iterator gate; capacity&gt;=16 heap string release, node free, nonzero count decrement. Full-tree cleanup/owner/game effects VERIFY |
| [0x00416870](symbols/00416870.md) | func | Tree_ClearFullRangeNodes | Original x86 full-tree recursive/iterative node destructor with nil guard and conditional heap string free. Caller 0x415CF0 resets header links and count=0; ownership/Spot+0xB8/game effects VERIFY |
| [0x004189B0](symbols/004189B0.md) | func | T028_ModeNonnegative_GatedSubobjectCall | Original PE 37B wrapper indirect vtable+0x64 gate, then ESI+0x1E0 and E8 0x5AA130; full ABI and gameplay VERIFY |
| [0x00419938](symbols/00419938.md) | code | SpotName_DrawTextReady | 0x597960呼出後の地名描画直前。EAXが文字列先頭、EBPが領地パネル、[EBP+0x1B8]が領地。天竜川上流域と実機一致。 |
| [0x0041EBE0](symbols/0041EBE0.md) | func | Variable_ModifyNumericDirect | 数値変数の参照を 0x463CA0 で取得した後、record+0x1C を直接更新する分岐を含む。 |
| [0x0041EF50](symbols/0041EF50.md) | func | Ai_SelectFourwayBattleMode | 四方向選択に使うグローバル 0x65EB64 をまず1へし、所有者の状態や条件により0へ切り替える。 |
| [0x00420900](symbols/00420900.md) | func | TrigCosNegSinToTwoInts | Original x86 70-byte trig helper: adds stored pi/2, calls cos and sin and integer converter, writes signed two-DWORD outputs to implicit ESI and ESI+4; conversion exceptions and gameplay role remain V |
| [0x00423D70](symbols/00423D70.md) | func | Image_GetChipRect | ECX=char* チップ名、ESI=出力RECT。0x879E68の要素+0x28〜+0x34を写す（無ければ0x8BE2E0〜の既定値） |
| [0x004243C0](symbols/004243C0.md) | func | Image_GetFaceCached | cdecl 引数1（char* 画像名）、EAX=HBITMAP。キャッシュ0x879E48を引き、無ければ0x427270で読み込んで登録 |
| [0x00424C80](symbols/00424C80.md) | func | Image_GetChipSprite | ECX=char* チップ名、EAX=HGDIOBJ。キャッシュ0x87A1B8、無ければ0x879E68の矩形から切り出してDIBを作り登録。表に無い名前は0 |
| [0x00427040](symbols/00427040.md) | func | Save_EncodeAdditiveEnvelope | 先頭4バイトのマジックと28バイト鍵を付け、32バイト目以降へ繰返し加算する共通エンコーダ。鍵生成で CRT rand を28回消費する。 |
| [0x004270F0](symbols/004270F0.md) | func | Save_DecodeAdditiveEnvelope | 01 02 03 04 のマジックを検査し、28バイト鍵でデータを減算復号した後に32バイトヘッダを除去する。 |
| [0x00428010](symbols/00428010.md) | func | Save_ReadGlobalVariables | global.sav を開いてバイト列を読み、復号・record 木への展開 0x429C60 に渡す。gread 命令から使われる。 |
| [0x00428710](symbols/00428710.md) | func | Save_WriteGlobalVariables | global.sav の既存レコードを読み、キーの値を upsert して全体を再直列化する。ゼロ値を書いてもキー削除とはならない。 |
| [0x00428F84](symbols/00428F84.md) | code | Save_WriteGlobalFileBytes | global.sav 更新後に WriteFile を呼び出し、再構築したストリームをディスクへ出力する箇所。 |
| [0x00429C60](symbols/00429C60.md) | func | Save_DecodeGlobalRecords | global.sav 読込後のデータを復号・解析し、キーと補助文字列とint32値の記録木に展開する補助。 |
| [0x0042F860](symbols/0042F860.md) | func | StdString_NotEqualsCStr | std::string と C 文字列を比べ、**違えば真**を返す |
| [0x00431BE0](symbols/00431BE0.md) | func | ResultFlag_GatedStackALWrapper | Bounded original x86 tests vtable+0x64 predicate then reloads AL from stack argument, passes receiver+0x260 to 0x5AA6E0; dynamic result VERIFY |
| [0x00431FB0](symbols/00431FB0.md) | func | FastSim_PreselectorRangeGate | Original x86 checks two index/begin/end ranges and 0x80000008 sentinels through implicit EAX; caller 0x40E25E branches on AL. Full ABI, field meaning and runtime reachability VERIFY. |
| [0x00432EE0](symbols/00432EE0.md) | func | Script_FireGameHook | ゲーム側からイベントを起動する仕組み（world/fight/politics フック） |
| [0x00433203](symbols/00433203.md) | code | Event_InstallPhaseFrames | phase dispatcher 内のフレーム設定位置。4本の並列 VM vector に追加または先頭挿入する。 |
| [0x004335E0](symbols/004335E0.md) | func | Event_RunExecutionMode | スクリプト実行の現在モード engine+0x1EEC3C によって mode1/2/6 などを分岐する実行経路。 |
| [0x004335FA](symbols/004335FA.md) | code | Event_TestBattleActiveGate | mode2 の内部分岐。engine+0x1EEC44 の byte を読み、戦闘更新後も再検査して VM runner を分岐する。 |
| [0x00433754](symbols/00433754.md) | code | Script_ExecEntry_Other | 0x4A1250 への 3 つ目の CALL。2026-11-03 の記録では通らなかった。 |
| [0x004338D0](symbols/004338D0.md) | func | Script_RunPass | スクリプトの主インタプリタ（1 パス分を実行） |
| [0x004339B1](symbols/004339B1.md) | code | Script_FetchCurrentFrame | インタプリタ内部で4本の並列 VM vector の末尾要素を現在フレームとして読む位置。 |
| [0x00433A2A](symbols/00433A2A.md) | code | Script_PopCompletedFrame | フレーム終了処理 0x433A2A..0x433A80 の内部位置。4本の vector の end pointer を各4バイト戻す。 |
| [0x00433B62](symbols/00433B62.md) | code | Script_ExecEntry_Field | 命令の実行本体 0x4A1250 への CALL。戦闘外の DAT 命令はここを通る（汎用一覧の入口）。 |
| [0x00433E80](symbols/00433E80.md) | func | Event_ExecuteMode6Branch | 実行モード6で通常のスクリプト実行ループから tail-jump される処理。 |
| [0x00435550](symbols/00435550.md) | func | Save_ReadWorldGraphState | 通常ロードの後半に世界側+0x504の状態を復元する。0x435C10 の書込経路と対応する。 |
| [0x00435C10](symbols/00435C10.md) | func | Save_WriteWorldGraphState | 通常セーブで世界側+0x504の状態を出力する。Spot経路等の保存グループに関係する。 |
| [0x00436080](symbols/00436080.md) | func | Event_TransformScriptFrame | 実行フレームを構築する補助関数の一つ。frameInstallMode=0 と通常実行の分岐に使われる。 |
| [0x004365F0](symbols/004365F0.md) | func | Event_InsertFrameKindZero | スクリプト実行フレームの構築時に引数0を配列の先頭へ挿入する補助。フレーム種類と命令位置の扱いに関係する。 |
| [0x00436870](symbols/00436870.md) | func | Text_Prepare_436870 | ボタンの文字などを用意する（推定） |
| [0x0043B5A0](symbols/0043B5A0.md) | func | ExpresElement_IsString_False | 常に偽を返す関数（TempStatusWnd の vtable +0x1C にも使われる） |
| [0x004479DF](symbols/004479DF.md) | code | Enemy_Vf03_StaleTroopRead | Enemy::vf03 0x447810 内の cmp byte [eax+0x1D],0。簡易戦闘で battle{} を設置すると、0x492890 が画面ありの戦闘用の陣営に vtable+0x0C を呼び、ここで古いデータを読んで落ちた（実機 1 回、例外 0xC0000005） |
| [0x00448E90](symbols/00448E90.md) | func | ModeScoreRank_Process | mode==2の候補+0xA0Cと他modeの+0xA10を比較子0x447240/0x447260へ分け、候補順位を更新する経路。最終targetは未証明。 |
| [0x00449500](symbols/00449500.md) | func | BattleCategory_UpdateUnitCandidates | カテゴリlabel・係数とeligible Unit配列の反復writer呼出し。category3入力のABIと実行後行動は未確定。 |
| [0x0044CF80](symbols/0044CF80.md) | func | Ai_DispatchMode1UnitGroup | mode1 の経路から Unit 群の仮想関数表 +0x68 を引数1で呼び出す。対象クラスとゲーム上の意味は未確定。 |
| [0x0044DCE0](symbols/0044DCE0.md) | func | Expression_EvaluateLogicalShortCircuit | 式の論理積（AND）と論理和（OR）を認識し、左辺の評価結果によって右辺の評価を省略する。 |
| [0x0044E3F0](symbols/0044E3F0.md) | func | Expression_RegisterConditionNames | isWorld、isNewTurn、isComTurn などの条件式名と opcode の登録を行う領域の入口。 |
| [0x0044F470](symbols/0044F470.md) | func | Event_EvaluatePhasePredicate | イベントのフェーズ条件やターン条件を評価する処理領域。個別の opcode 分岐があり、各条件の入力には現在の実行モードが影響する。 |
| [0x004518FA](symbols/004518FA.md) | code | Expression_GetBattleTime | getTime 条件（opcode0x25A）で engine+0x1EED60 を返す分岐位置。 |
| [0x0045190B](symbols/0045190B.md) | code | Expression_GetBattleLimit | getLimit 条件（opcode0x25B）で 0x565730 を呼び現在の時間制限を取得する。 |
| [0x00451915](symbols/00451915.md) | code | Expression_TestBattleInterval | isInterval（opcode0x25C）で正の指定値を10の倍数に切り上げ、engine+0x1EED64 の割り切れ判定に使う。 |
| [0x00452D90](symbols/00452D90.md) | func | BattleWnd_PrimaryDrawEligibilityVCall | Original primary vtable+0x0C gate: with nonzero byte arg and ECX+0xA4!=0x80000008 returns AL=0, otherwise returns byte [ECX+0x84] (RET4); actual draw/runtime vptr VERIFY. |
| [0x00455520](symbols/00455520.md) | func | FrameWnd_DrawButtonText | ボタンの枠と文字をウィンドウの画像に描く（BitBlt/AlphaBlend と DrawText）。EAX=ウィンドウ、ESI=矩形、引数 (描画先, 文字)、ret 8。ボタンの当たり判定はしない |
| [0x00455CF0](symbols/00455CF0.md) | func | FrameWnd::vf12_shared43 | ウィンドウ共通のマウス移動処理。TempStatusWnd では説明表示に届かない（+0x44 が空の関数） |
| [0x00455D90](symbols/00455D90.md) | func | FrameWnd_ScreenToLocal | 画面座標をウィンドウ内の座標へ変換（推定） |
| [0x004591F0](symbols/004591F0.md) | func | UnitData_DestroyPayload | UnitData 相当の記録内にある複数の文字列・vector を解放する。ノード自体の free より前に実行される。 |
| [0x0045B850](symbols/0045B850.md) | func | Game_Start | ゲーム開始 |
| [0x0045BE10](symbols/0045BE10.md) | func | Scenario_InitialPlacement | シナリオ開始時の配置 |
| [0x0045E1E0](symbols/0045E1E0.md) | func | Save_LoadReaderCore | 通常 .sav のロード時に Unit・Spot などの一時領域を初期化し、見出し→数値変数→Unit→Spot→Power→ターン進行→世界地図グラフの順に読む。グラフ 0x435550 の後で戻り、残りのバイトは見ない。 |
| [0x0045E5F0](symbols/0045E5F0.md) | func | Save_LoadFileAndDecode | セーブファイル全体を読み（GetFileSize→ReadFile）0x4270F0 で復号して 0x45E1E0 へ渡す。ファイル長と本体の長さを比べない。開けないときは LoadException を投げる |
| [0x0045E7F0](symbols/0045E7F0.md) | func | Save_LoadFullState | 通常セーブの復元経路。ファイルを復号した後、既存の数値変数の木を解放し、保存グループを再構築する。 |
| [0x0045EAC0](symbols/0045EAC0.md) | func | Save_LoadStoredGroups | 通常ロード中の保存グループを解析する処理。script数値変数の木を含む複数のコンテナを読み直す。 |
| [0x0045F960](symbols/0045F960.md) | func | Save_PrepareFullMetadata | 通常保存用のメタデータと状態を組み立て、0x460000 の writer に渡す。 |
| [0x0045FD3E](symbols/0045FD3E.md) | code | Save_HeaderGetLocalTime | 保存の見出し用に GetLocalTime を呼ぶ位置。直後に wMonth の上位 8 ビットへ (wYear+0x30) を詰める（2026 年 10 月 → 0x1A0A） |
| [0x0045FF4B](symbols/0045FF4B.md) | code | Save_WriteAutosaveSlot | auto.sav を作る保存経路で通常 writer 0x460000 にファイル名を渡す位置。 |
| [0x00460000](symbols/00460000.md) | func | Save_WriteFullState | 通常 .sav のエンジン状態をグループ順に直列化し、0x427040 の共通エンベロープで暗号化して書き込む。OPEN_ALWAYS で切り詰めないため、既存ファイルより短く書くと古い末尾が残る（実セーブ save3・auto で実測）。 保存済み著者の局所静的報告ではstream状態mask非0でもWriteFileへ至る分岐が残る。実行時bytecount・書込成功・破損・上位通知は未確認。 |
| [0x0046065C](symbols/0046065C.md) | code | Save_EncryptStreamBeforeWrite | 通常セーブのファイル書込み直前に共通エンコーダ 0x427040 を呼ぶ位置。 |
| [0x00460E90](symbols/00460E90.md) | func | UnitDef_SetRoaming | ユニットを放浪させる（def+0x84 に放浪先、ctx+0x32C の集合へ追加） |
| [0x00460F10](symbols/00460F10.md) | func | UnitDef_ClearRoaming | 放浪を解除する |
| [0x00461DA0](symbols/00461DA0.md) | func | World_MonthlyRoamMove | 月次の放浪移動 |
| [0x00463610](symbols/00463610.md) | func | Variable_WriteScenarioName | 起動時の @scenario 用に呼ばれる別の変数 writer。@gamemode の数値変数経路とは異なる。 |
| [0x004637A0](symbols/004637A0.md) | func | Variable_WriteNumericMap | スクリプトの永続数値変数を engine+0x30C/+0x310 のmapへ書き込む。pushRand などの命令からも呼ばれる。 |
| [0x00463CA0](symbols/00463CA0.md) | func | Variable_GetOrCreateNumeric | スクリプト数値変数を名前で検索し、存在しなければ値+0x1Cを0にした新レコードを作る。 |
| [0x00464290](symbols/00464290.md) | func | Prop_LookupBase | プロパティの有無を調べる（has_key） |
| [0x0046453F](symbols/0046453F.md) | code | ScriptData_SuperParentLookupPresenceSite | Original x86/V9 E8 to 0x4C1200 after local optional-parent name checks; all caller and inheritance meaning VERIFY. |
| [0x004647D0](symbols/004647D0.md) | func | Prop_LookupString | プロパティの文字列を引く（lookup） |
| [0x00466BA0](symbols/00466BA0.md) | func | UnitData_CopyRecordPayload | UnitData 相当の値オブジェクトをコピーして召喚記録の引数や木ノードに構築する。 |
| [0x00466F60](symbols/00466F60.md) | func | UnitDef_CreateMember | member（配下）の def を再帰的に生成 |
| [0x00467DE0](symbols/00467DE0.md) | func | UnitData_FindPersistentRecord | 永続化側の context+0x300 の木を検索し、node+0x28 に格納された UnitData* を返す。 |
| [0x00467E90](symbols/00467E90.md) | func | Spot_FindByName | 保存済み報告が独立したSpot名前解決関数として示す。CtxのSpot表を検索し、見つかったSpot+0xB0にCtxを設定して返す。未発見はnull。今回の原作再検証なし。 |
| [0x00467F40](symbols/00467F40.md) | func | Power_FindByName | 保存済み報告ではCtxのPower表を名前検索し、返却Power+0xE0にCtxを設定する。旧Spot名はF§49の未確定な解釈。完全ABI・実機動作は未検証。 |
| [0x00470550](symbols/00470550.md) | func | Save_ReadSlotHeader | 通常セーブの見出しを読む。文字列 2 本の後の u32 を第 3 引数へ、続く u32 4 個を SYSTEMTIME の wMonth・wDay・wHour・wMinute へ入れる。呼出元は通常ロード 0x45E2D8 と 0x45ECBB・0x4CFC2A・0x539364 |
| [0x004705F0](symbols/004705F0.md) | func | Save_ReadPrintableString | 保存ストリームからNUL終端の印字可能文字列を読み取る。数値mapのキー・補助文字列にも使われる。 |
| [0x00470700](symbols/00470700.md) | func | Save_ReadInt32Value | 通常セーブの数値map復元時に32bit値を読むヘルパー。文字列2本の直後に呼ばれる。 |
| [0x00470830](symbols/00470830.md) | func | Save_WritePrintableString | 0x20〜0x7F の文字を検査してNUL終端の文字列を保存ストリームへ出す。 |
| [0x004708A0](symbols/004708A0.md) | func | Save_WriteByteAsU32 | 1 バイトの値をゼロ拡張して 4 バイトで保存ストリームへ書く（Unit+0x74〜0x7A・+0xE8、Power+0x1C・+0x1D、ターン進行+0x09・+0x0A など） |
| [0x004708D0](symbols/004708D0.md) | func | Save_WriteSlotHeader | 通常セーブ先頭の見出しを書く。並びは @gamemode の値、シナリオ名、勢力名、ターン進行+0x14、保存日時（年を詰めた月・日・時・分を各 u32）。時・分の部分 0x470945〜0x47096E は保存命令で確認、全体の並びは読込 0x470550 と実セーブ 4 件で照合 |
| [0x004716C0](symbols/004716C0.md) | func | Turn_Init | ターンの初期化 |
| [0x00471AF0](symbols/00471AF0.md) | func | Save_ReadTurnState | 通常セーブの後段でターン進行オブジェクト（G+0x1EF4B4）の +0x09・+0x0A・+0x14（経過ターン）・+0x38（phase）と手番順の勢力列を読む。旧名 Save_ReadDiplomacyState は誤り。 |
| [0x00471D20](symbols/00471D20.md) | func | Save_WriteTurnState | 通常セーブの後段でターン進行オブジェクト（G+0x1EF4B4）を書く。0x471AF0 と対。旧名 Save_WriteDiplomacyState は誤り。 |
| [0x00471E80](symbols/00471E80.md) | func | Turn_Process | ターン処理（人材の行動・出奔・外交の拒否など） |
| [0x00474F10](symbols/00474F10.md) | func | GameCtrl::vf01 | ターンの全体を回す処理（GameCtrl の仮想関数） |
| [0x00475C60](symbols/00475C60.md) | func | EmployHero_Answer | employ_hero の回答処理 |
| [0x00476D60](symbols/00476D60.md) | func | PowerAI_Hire | 勢力 AI の雇用 |
| [0x00479740](symbols/00479740.md) | func | Random_ShuffleStringVector | スクリプト shuffle の文字列ベクトルを並べ替える補助。0x479A30 を呼び、28バイト要素の Fisher-Yates 処理に接続する。 |
| [0x00479A30](symbols/00479A30.md) | func | Native_VectorShuffle | std::random_shuffle（0x1C 文字列） |
| [0x0047A1A0](symbols/0047A1A0.md) | func | PowerAI_Reassign | 勢力 AI の配置換え |
| [0x0047BB50](symbols/0047BB50.md) | func | ComparatorSort_SmallInsertionLargePartition | 候補ポインタ配列と関数ポインタ比較子を受けるsort。2..32件は0x44D6A0挿入経路、33件以上は0x47BCC0分割・再帰経路。T013のmode別signed比較子から呼ばれるが公開ABI・多件数の同点安定性・最終targetは未検証。 |
| [0x0047C280](symbols/0047C280.md) | func | Turn_Phase_47C280 | ターン構造の一部（§64.1 参照） |
| [0x0047D770](symbols/0047D770.md) | func | Talent_WarStartAndDesert | 人材の戦争開始と出奔 |
| [0x0047E3A0](symbols/0047E3A0.md) | func | PowerAI_SelectTarget | 勢力 AI の目標選定 |
| [0x00481260](symbols/00481260.md) | func | PowerAI_Diplomacy | 勢力 AI の外交 |
| [0x0048ABF0](symbols/0048ABF0.md) | func | Battle_ClearUnitTables | 評価器の +0x1EEBE0/+0x1EEBF0 の木を空にする（戦闘の後片付けと推定）。 |
| [0x0048AD30](symbols/0048AD30.md) | func | Title_Handler | 場面 0（タイトル）の処理。'title_name' を使う |
| [0x0048B4A0](symbols/0048B4A0.md) | func | Scene_RunRngResetBranch | 場面更新の途中で0x48B658から共通の乱数リセットを呼ぶ分岐を含む。場面番号による実際の用途は未確認。 |
| [0x0048BC70](symbols/0048BC70.md) | func | Scene_RunPhase6SeedSetup | 実行フェーズ6を設定し、0x48BCB9で乱数リセット補助を呼ぶ。フェーズ5側とは別の分岐。 |
| [0x0048BF60](symbols/0048BF60.md) | func | Scene_RunPhase5SeedSetup | 実行フェーズ5を設定した後、0x48BFECで共通リセット0x4C1FC0を呼び、0x48BFF8で後続補助0x4C2240を呼ぶ。旧ロード一般処理という説明は過大だった。 |
| [0x0048C880](symbols/0048C880.md) | func | Event_RunWorldPhase | World の場面更新を行う入口の一つ。GameManager の場面切替から呼ばれ、world phase dispatchへ進む。 |
| [0x0048D6A0](symbols/0048D6A0.md) | func | Battle_ConstructScene | 通常戦闘のscene2構築関数。GameEvent 相当を受けてUnit/Map・乱数・Task・VMの初期化へ進み、実際の通常復帰RETは0x48EA5Aにある（旧Ghidraの0x48EA38終端説は誤り）。 |
| [0x0048EEE0](symbols/0048EEE0.md) | func | Audio_StartWorldPlaylist | World 側の BGM 候補を作成し、world-music flagが立っていれば二重開始を避ける。 |
| [0x0048F080](symbols/0048F080.md) | func | Audio_SelectBattleEventBgm | 戦闘イベントの bgm プロパティを調べ、空でなければ custom BGM 名として 0x4BDE40 に渡す。none の特別扱いはない。 |
| [0x0048F720](symbols/0048F720.md) | func | ListTree_FindFirstNonmemberFlaggedRecord | EAX outer candidates plus stack context; distinct sentinel offsets +0x21 outer / +0x19 exclusion / +0x11 inner; unsigned exclusion compare; if outer key is not excluded AND node+0x18 inner count&gt;0, |
| [0x0048F9E0](symbols/0048F9E0.md) | func | War_Start | 戦争開始 |
| [0x004922A0](symbols/004922A0.md) | func | Battle_Begin | 戦闘の開始（簡易戦闘の後に fight）。通常は 0x4922A0(GM, skip) から |
| [0x00492710](symbols/00492710.md) | func | Event_InitializeBattleClock | 戦闘開始時に engine+0x1EED60（resetTime対象）と +0x1EED64（interval基準）を両方0へ戻す。 |
| [0x00492890](symbols/00492890.md) | func | BattleEvent_InstallBattleBlock | ScriptBattle の処理。モード2・active1 を書いたあと、画面ありの戦闘用の 3 陣営 E+0x1E8630/34/38 の vtable+0x0C を無条件に呼ぶ（0x492A43..0x492A65）。簡易戦闘ではこれが原因で落ちることがある |
| [0x00492960](symbols/00492960.md) | code | Event_SetBattleExecutionMode_ReportedSite | 回収済みT010報告が戦闘setupとして示す位置。engine+0x1EEC3Cに2を設定すると記載。関数入口ではなく、命令位置・境界の原作再検証なし。 |
| [0x00492D80](symbols/00492D80.md) | func | Event_ProcessBattleTick | 戦闘の進行に合わせた処理経路。自然終了判定と ScriptVM の再開に関連する入口として参照される。 |
| [0x004930C0](symbols/004930C0.md) | func | Event_EvaluateBattleIfRoots | 戦闘に登録された if/rif のroot条件を評価する。真の通常ifは実行後に集合から除去し、rifは残す。 |
| [0x0049356A](symbols/0049356A.md) | code | Script_ExecEntry_Battle | 0x4A1250 への CALL。戦闘中の battleEvent と dead_event の命令はここを通る。dead_event は倒れたその場で実行。 |
| [0x00493630](symbols/00493630.md) | func | Battle_End | 戦闘終了（勝敗の反映・戦略への復帰） |
| [0x0049CD60](symbols/0049CD60.md) | func | Ai_UpdateKeyedUnitVector | キー付きベクトルを検索・消去・挿入する関数群の入口。書換えで使われる値の名称と全分岐は未確定。 |
| [0x0049D1B0](symbols/0049D1B0.md) | func | Ai_Mode1PrepassVectorDrain | Native 163B prepass vector iteration through virtual +0x58, conditional +0x24 notification and logical end reset; other callers, ABI and runtime outcomes VERIFY |
| [0x0049E560](symbols/0049E560.md) | func | Battle_RegisterUnitName | BattleUnit を評価器+0x1EEBEC(名前)と+0x1EEBDC(UnitData)の表に登録。通常型 0x56F880・簡易型 0x544290 の両コンストラクタから。召喚獣も登録される。 |
| [0x0049E780](symbols/0049E780.md) | func | Battle_FindUnitByName | __fastcall(ECX=名前, EDX=評価器=context+0x504)。評価器+0x1EEBEC の multimap(名前→BattleUnit)を引き、生存(+0x1867C=0)を優先、なければ最初の倒れたユニットを返す。isDead/getDistance/getLife/skillTroop など19か所が使う。 |
| [0x0049E8B0](symbols/0049E8B0.md) | func | Ai_CollectAliveUnitsFromTree | 木構造のユニット参照を走査し、Unit+0x1867C!=0 の死亡扱いを除外して生存ユニットを配列に集める。 |
| [0x0049ED90](symbols/0049ED90.md) | func | TreeHeader_InitSentinel | 訓練bonus局所mapのheader初期化呼出先。24-byte sentinelを自己リンクしcount=0。汎用treeの型と失敗時処理は未確定。 |
| [0x0049F7D0](symbols/0049F7D0.md) | func | Ai_InsertKeyedVectorRecord | キー付きベクトルを格納する木への挿入処理を担当する。record+0x1C の3ポインタの引継ぎを含む。 |
| [0x004A1250](symbols/004A1250.md) | func | Script_DispatchCommand | GENERAL 命令の分岐（79 命令） |
| [0x004A17C8](symbols/004A17C8.md) | code | Save_DispatchCommand | スクリプト save（opcode7）の処理入口で 0x45F960 へ状態を渡す。 |
| [0x004A17D8](symbols/004A17D8.md) | code | Script_Op_Wait | wait 命令（op9） |
| [0x004A18B1](symbols/004A18B1.md) | code | Event_DispatchBattleEvent | スクリプト battleEvent（opcode10）でrootを列挙し、ScriptIF のみを active list に登録する位置。 |
| [0x004A2793](symbols/004A2793.md) | code | World_DispatchSkinRebuild | スクリプト worldskin（opcode24）の処理位置。derived world skin を作り直す 0x5B47B0 を呼ぶ。 |
| [0x004A2ED6](symbols/004A2ED6.md) | code | Spot_DispatchShowSpot | スクリプト showSpot（opcode42）の処理位置。Spot 表示オブジェクトを取得または生成して表示する。 |
| [0x004A304A](symbols/004A304A.md) | code | Spot_DispatchHideSpot | スクリプト hideSpot（opcode43）の処理位置。既存Spotの表示オブジェクトの非表示処理を呼ぶ。 |
| [0x004A5F53](symbols/004A5F53.md) | code | Variable_DispatchGread | スクリプト gread（opcode0x4C）から global.sav の読込 0x428010 を呼ぶ分岐位置。 |
| [0x004A60D1](symbols/004A60D1.md) | code | Variable_DispatchGwrite | スクリプト gwrite（opcode0x4D）から global.sav 更新 0x428710 を呼ぶ分岐位置。 |
| [0x004A6E40](symbols/004A6E40.md) | func | World_RegisterPowerCommands | World 側の勢力操作コマンド用の名前・関数登録領域。unionPower と addPower が同じ engine+0x1EEF60 の登録集合へ入る。 |
| [0x004A6FE1](symbols/004A6FE1.md) | code | Power_RegisterAddPower | 同じ World builtin 登録領域で addPower コマンドの名前を登録する命令位置。 |
| [0x004A71AA](symbols/004A71AA.md) | code | Power_RegisterUnionPower | World の builtin 登録領域で unionPower コマンドの名前を登録する命令位置。 |
| [0x004A7A90](symbols/004A7A90.md) | func | Script_DispatchWorldCommand | WORLD 命令の分岐（52 命令） |
| [0x004AE0F0](symbols/004AE0F0.md) | func | Script_DispatchVarCommand | VARIABLE 命令の分岐 |
| [0x004AEDDA](symbols/004AEDDA.md) | code | Random_DispatchPushRand | pushRand（opcode14）で0〜99の乱数を生成し、スクリプト数値変数へ書き込む命令入口。 |
| [0x004B044F](symbols/004B044F.md) | code | Random_DispatchShuffle | shuffle（opcode40）で文字列ベクトルの存在を確認し、0x479740 から並び替えを実行する位置。 |
| [0x004B4645](symbols/004B4645.md) | code | Battle_SkillTroopRegistrationSite | 部隊/battle builtin登録表ではskillTroopをdecimal opcode14へ結ぶ登録位置。処理handler位置0x4B608Fとは別。原表の対応を採録し、完全関数境界・引数ABI・効果を確定しない。 |
| [0x004B47FC](symbols/004B47FC.md) | code | Event_ResetBattleClock | resetTime 命令の処理位置。engine+0x1EED60 だけを0にし、interval時計+0x1EED64は変更しない。 |
| [0x004B608F](symbols/004B608F.md) | code | Battle_SkillTroopHandlerSite | 部隊命令表のhex0E(decimal14) skillTroopに対応するhandler位置。登録位置0x4B4645と区別し、main命令の同じ番号と混同しない。関数入口・引数ABI・副作用は未確認。 |
| [0x004B9930](symbols/004B9930.md) | func | Scene_DispatchGameMode | GameManager が場面番号 +0x1EF144 の0〜7に応じて処理を分岐する経路。World 側は 0x48C880 へつながる。 |
| [0x004B9AA0](symbols/004B9AA0.md) | func | Input_HandleEscapeExit | Esc の押下とアクティブ状態を検査し、ウィンドウ表示モードに応じた終了・確認処理へ進む。 |
| [0x004B9AD0](symbols/004B9AD0.md) | code | Title_Continue | タイトルの「続きから」側の分岐（DLL のタイトル判定で使用） |
| [0x004B9B73](symbols/004B9B73.md) | code | Title_Return | タイトルへ戻る側の分岐 |
| [0x004B9E50](symbols/004B9E50.md) | func | Input_CreateNewGameMouseHost | NewGameMouse を確保・初期化してプレイヤーの入力参照に設定する経路を含む。 |
| [0x004BBAE0](symbols/004BBAE0.md) | func | Input_DestroyMouseHost | GameMouseのホスト終了側で関連デバイス・参照を解放する。global hostのvtableとの関連を持つ。 |
| [0x004BCF20](symbols/004BCF20.md) | func | Input_ReleaseGameMouseResource | GameMouse の RTTI 仮想関数表に登録された先頭メソッド。詳細な解放対象は未確認。 |
| [0x004BCF70](symbols/004BCF70.md) | func | Input_PollGameMouse | GameMouse の DirectInput バッファ入力を取得する。0x879822==0 の非アクティブ時はedge状態を消してpollを省く。 |
| [0x004BD170](symbols/004BD170.md) | func | Input_FlushInactiveDevices | 非アクティブ遷移で2つの buffered DirectInput デバイスをフラッシュする。両デバイスの仮想関数表+0x28を呼ぶ。 |
| [0x004BD2A0](symbols/004BD2A0.md) | func | Audio_RefreshMasterVolumeState | マスター音量用の基準値キャッシュの更新に関係する補助。実際の音量適用順序は複数の経路に分かれる。 |
| [0x004BDE40](symbols/004BDE40.md) | func | Audio_StartBgmTrack | BGM の直接再生コア。ECX にファイル名を受け、スタック6引数を処理する（ret 0x18）。 |
| [0x004BE220](symbols/004BE220.md) | func | Audio_AdvancePlaylistOnEnd | BGMの再生状態を調べ、再生完了や停止の際に0x4BF2B0でリセットし、次の曲を0x4BDE40で開く。1曲だけのloopでも再オープンが生じる。 |
| [0x004BE340](symbols/004BE340.md) | func | Audio_UpdateMasterVolumeSlider | UIのマスター音量から減衰値を作る。ゼロ指定は内部で -10000 として扱い、その後有効下限 -9600 に収める。 |
| [0x004BE388](symbols/004BE388.md) | global | g_InputReceiver | 入力pollの受け手。vtable 0x6394A0、vtable+4 が0x4EE170、+8 がDirectInputの消費側。DLLの入力保護がこの呼出しの後で動く |
| [0x004BE3E0](symbols/004BE3E0.md) | func | Audio_ApplyScriptVolume | スクリプト volume の値を変換する。正値は百分率、ゼロ以下は生減衰値として扱い、最終値を -9600〜0 に制限する。 |
| [0x004BE480](symbols/004BE480.md) | func | Audio_OpenCodecBackend | MP3等の再生バックエンドを初期化し、必要な内部バッファとDirectShow等のインターフェースを用意する。 |
| [0x004BE820](symbols/004BE820.md) | func | Audio_PrepareBgmPlayback | BGM再生開始中の曲選択・既存再生状態に関する補助。既存曲・空曲で遷移が分かれる。 |
| [0x004BF2B0](symbols/004BF2B0.md) | func | Audio_StopResetCurrentTrack | BGMプレイヤーの停止・リセット処理。プレイリスト切替時に呼び出される。 |
| [0x004BF410](symbols/004BF410.md) | func | Audio_ProcessFadeOutCompletion | BGMのフェードがゼロへ到達した後、停止・リセット・保存済み曲の再オープンへ分岐する。 |
| [0x004BF520](symbols/004BF520.md) | func | Audio_SetFadeTransitionState | BGMのフェード入力を設定する補助。player+0x20 の符号と停止・再開条件を区別する。 |
| [0x004BF570](symbols/004BF570.md) | func | Audio_ResumeBgmTransition | 再生コアの既存曲・空曲条件に応じた後続遷移を処理する。開始音量の経路は条件付き。 |
| [0x004BF630](symbols/004BF630.md) | func | Audio_ApplyAttenuationToBackend | 現在の音声バックエンドへ音量減衰値を設定する。ここ自体は曲を停止・再オープンしない。 |
| [0x004BF6A0](symbols/004BF6A0.md) | func | Audio_TestTrackTransitionGate | 再生完了や停止条件でプレイリスト遷移を許すか検査する補助。正確な codec ごとの条件は未検証。 |
| [0x004BF720](symbols/004BF720.md) | func | Audio_ResolveTransportBranch | BGMの状態下位5bitとフェード・EOF判定で次の処理を選ぶ。 |
| [0x004BF780](symbols/004BF780.md) | func | Audio_TransitionPlaylistAfterEof | プレイリストの再生終了判定側で呼ばれ、次曲へ移行する処理に接続する。codecごとの条件がある。 |
| [0x004C1200](symbols/004C1200.md) | func | Variable_FindTreeKey | 汎用木のキー検索に用いられる関数。文字列比較を通じて候補nodeと番兵を判別する。 |
| [0x004C1FC0](symbols/004C1FC0.md) | func | Random_InitializeMapSeed | マップの乱数初期化の経路。内部から CRT srand を呼び、別のマップ初期化ステップにも接続する。 |
| [0x004C21F0](symbols/004C21F0.md) | func | GameTask_SetFps | thiscall、引数 fps。GameTask+0x74=fps、+0x78=round(1000/fps)。0x48AA00は25、0x513C60・0x526A40は25と100を切り替え |
| [0x004C2240](symbols/004C2240.md) | func | Vector32_Append_4C2240 | 保存済み局所解析では、owner+0x64/+0x68/+0x6Cで管理する4B要素vectorへ値を追加する補助。Bの呼出し箇所はTask待機列の文脈。旧T031のscene乱数reset後の呼出し記録を、callee自体の乱数専用処理とは一般化しない。全caller型・実機動作は未確認。 |
| [0x004C24B0](symbols/004C24B0.md) | func | Window_PumpGameLoop | ゲームのメインループ。未処理メッセージを全部処理してから1コマ進める。1コマ：timeGetTime→GameTask+0x78との差だけSleep→0xAC0918へ時刻→更新→描画0x4C3EB0→Present。非アクティブ時は10msのSleepだけ |
| [0x004C5800](symbols/004C5800.md) | func | List_SpliceWithCapacityGuard | 異なるlist間でnodeを移して双方の+4 countを更新、0x3FFFFFFE超過条件で別処理へ分岐。Unit上限ではない。 |
| [0x004C7040](symbols/004C7040.md) | func | Ai_ApplyFourwayPairState | 四方向用の +0x48/+0x4A/+0x4C/+0x4E の各ペアを番号0〜3で処理する。実際のゲーム効果の意味は未確定。 |
| [0x004DEC70](symbols/004DEC70.md) | func | Tree_EraseIteratorNode | 部分範囲消去側の単一node削除下位処理。node+0x15のiterator検査、freeとcount条件減算。通常の訓練全消去では必達でない。 |
| [0x004DEF40](symbols/004DEF40.md) | func | Tree_EraseRange | 先頭と終端を受ける範囲消去。全区間では0x4ED030、部分区間では0x4DEC70へ分岐。一般的なABIと異常系は未検証。 |
| [0x004DFBB0](symbols/004DFBB0.md) | func | SkillEffectRingRecord_InitializeAndDelegate | Original bounded x86: conditional old R record call, reset/copy 24-byte input records, linked vtable+0x28 and 0x41E060 calls, ret 0xC; child effects and arbitrary count safety VERIFY |
| [0x004E04F0](symbols/004E04F0.md) | func | RetreatVoice_Update | RetreatVoiceのTask更新という保存チャットの著者報告。+0x70の負/0/正で待機・再配置・上移動を分け、正のcounterが64を超えると0へ戻す。+0x5Cは減算後0へclamp。表示/音声の実機対応・全ABIは未確認。 |
| [0x004E4C70](symbols/004E4C70.md) | func | Unit_ApplyKnockMovementHelper | ノックバック時の位置移動補助として 0x57AC5C 以降から使われる。移動可能残量の分岐の後で呼ばれる。 |
| [0x004E4F60](symbols/004E4F60.md) | func | SpatialCell_RemoveMatchingPointer | Native branch on +0x3C selects identity-gated scalar clear or matching-pointer vector removal; death/move direct callers; gameplay and ownership VERIFY |
| [0x004E53B0](symbols/004E53B0.md) | func | Unit_RefreshTargetLatch | Unit+0xC の参照元と本人を入力に取り、戻り値を Unit+0x1E570 に保存する処理で使われる。値の厳密な論理名は未確定。 |
| [0x004E70E0](symbols/004E70E0.md) | func | Summon_ProcessSharedQueue | 召喚処理と代替移動処理で共用される2DWORDの待ち行列を使う。末尾投入・先頭取得・先頭進行・件数減算を含む。 |
| [0x004E7ED0](symbols/004E7ED0.md) | func | Skill_CheckMissileRangeGate | 通常 missile のMP消費より前の対象・射程判定補助。探索窓と有効半径の参照値が分岐で変わる。 |
| [0x004EC1E0](symbols/004EC1E0.md) | func | RouteCache_ConditionalHitPromotion | Native hit recency relink only above 8000 records, eviction branch on count&gt;=8192; key ownership and runtime outcomes VERIFY |
| [0x004ED030](symbols/004ED030.md) | func | Tree_ClearAllNodes | 全区間tree消去の下位処理。0x49F6A0のsubtree解放とsentinel自己リンク復元、count=0を含む。 |
| [0x004EE0C0](symbols/004EE0C0.md) | func | Input_ConstructNewGameMouse | NewGameMouse の生成時に呼ばれる初期化関数。生成した実体は Player の入力参照へ配置される。 |
| [0x004EE110](symbols/004EE110.md) | func | Input_ResetNewGameMouse | NewGameMouse のマウス状態 +0x18〜+0x38 と14個のキーボードword +0x3C〜+0x57 を0へ戻し、デバイス再取得を呼ぶ。 |
| [0x004EE170](symbols/004EE170.md) | func | Input_ClearKeyEdgesBeforePoll | キーボードwordの上位edge byteを消し、下位heldを維持してから入力pollへ渡す。 |
| [0x004EE1B0](symbols/004EE1B0.md) | func | Input_ProcessBufferedKeys | NewGameMouse のキー状態を更新し、共有修飾キーword+0x50の押下・解放状態を処理する。 |
| [0x004F93A0](symbols/004F93A0.md) | func | Ai_ComputeBattleAreaTargetPoint | 戦闘領域の境界値と Unit 座標から候補座標を生成する補助。探索キャッシュの後段補正で呼ばれる。 |
| [0x005001B0](symbols/005001B0.md) | func | Random_SetMapGenerationSeed | マップ初期化に関わる乱数 seed 生成経路。0x49B191 から呼ばれ、CRT srand を実行する。 |
| [0x005023E0](symbols/005023E0.md) | func | Bgm_StreamThread | BGM ストリーム再生のスレッド |
| [0x00502DD0](symbols/00502DD0.md) | func | Lexer_NextToken | スクリプトの字句解析 |
| [0x005050EE](symbols/005050EE.md) | code | ScriptData_SuperEntryInsertCallSite | Original x86/V9 E8 to 0x463280 within conditional super ScriptData producer; duplicate keys and gameplay VERIFY. |
| [0x0050A5E0](symbols/0050A5E0.md) | code | Script_IfRifParserCallbackBinding | 制御構文if/rifの登録対応表で共通callback pointerと報告された位置。個々の登録site 0x50ECD2/0x50ED1Cとは別。完全関数境界・公開ABI・構文条件の実動作は未確認。 |
| [0x0050B220](symbols/0050B220.md) | func | Script_Loader | スクリプト読込器 |
| [0x00514AA0](symbols/00514AA0.md) | func | Battle_ReleaseSideUnitVectors | 陣営オブジェクトの +0x48・+0x58・+0x38 の3配列をたどり、非NULLユニットの仮想デストラクタに flag=1 を渡す。 |
| [0x00514C80](symbols/00514C80.md) | func | Battle_SideRemains | side+0x48..+0x4Cの適格候補を探索し、候補が見つかればAL0、なければAL1。isAllDead命令の最終boolや、同じ陣営の全型の全滅判定とは区別する。 |
| [0x00514D60](symbols/00514D60.md) | func | Ai_SelectNearestTarget | SimpleUnit と SimpleStaticUnit の二系統候補を距離で調べる。通常型の候補には Unit+0x1C0 の stealth% に応じた確率的除外がある。 |
| [0x00514F10](symbols/00514F10.md) | func | Ai_BuildSupportTargets | 生存する SimpleUnit 候補を列挙し、距離付き24バイトレコードを作る。通常分岐では candidate+0x1D0==0 を除外する。 |
| [0x00515060](symbols/00515060.md) | func | Ai_SumSupportUnitValues | SimpleUnit 配列を走査し、特定の Unit+0x1D0 条件によって値を集計する補助。集計値の厳密な名称は未確定。 |
| [0x00515150](symbols/00515150.md) | func | Ai_ReadSupportUnitIndex | 候補 Unit+0x1D8 を別配列の添字として使い、関連する値を取り出す処理を含む。配列の論理名は未同定。 |
| [0x005151D0](symbols/005151D0.md) | func | Ai_RebuildLiveUnitScoreMap | 容器の +0x28/+0x2C にある探索木を初期化し、生存する SimpleUnit の一覧を走査してスコア類を登録する。 |
| [0x005154F0](symbols/005154F0.md) | func | Ai_AppendCandidateRecord | 24バイト候補レコードの追加・コピーに使われるベクトル補助。目標の評価順位付け本体ではない。 |
| [0x005158A0](symbols/005158A0.md) | func | Ai_CopySupportFallbackRecords | 支援候補レコードのコピーに関与する補助。探索コアの分岐によっては呼ばれない経路がある。 |
| [0x00521560](symbols/00521560.md) | func | Player_DispatchHover | 説明表示の振り分け。イベント実行中は vfunc+0x1C が真のウィンドウにだけ渡す。マウス位置は Player+0x324/+0x328（ゲーム座標）でウィンドウ矩形と比べる |
| [0x00521A00](symbols/00521A00.md) | func | Player::b144_vf01 | プレイヤーの毎フレーム処理（+144 にある Actionable 側の仮想関数表の 1 番。2026-10-11 の名前 Player::vf01 は主表と区別していなかった） |
| [0x00521AF0](symbols/00521AF0.md) | code | Player_HoverCallSite | 0x521560 を呼ぶ位置（Work の CALL 差し替えの候補） |
| [0x00526030](symbols/00526030.md) | func | GroupFirstEligibleUnit_DistanceCompare | Calls square-root helper and compares bounded original-x86 distance intermediates with FCOMP/TEST AH,0x41; Unit+0x1867C test; 32-bit wrap/FP exceptional order and gameplay outcome VERIFY |
| [0x00526510](symbols/00526510.md) | func | Input_HandleBattlePauseRequest | 戦闘画面の Space または中央操作による pause要求を処理する。選択対象処理より先に呼ばれる。 |
| [0x00526A40](symbols/00526A40.md) | func | Input_HandleBattleSpeedShortcut | 戦闘操作中にZキーのheld/edgeを調べ、関連する速度状態に応じて入力を処理する。 |
| [0x00526E50](symbols/00526E50.md) | func | Input_ProcessSelectedUnitCommand | プレイヤーの選択部隊が存在する場合に優先される命令処理の一つ。World座標への変換経路へつながる。 |
| [0x005271A0](symbols/005271A0.md) | func | Input_ResolveBattleWorldPoint | ユニットへの命令操作で画面座標からワールド座標へ変換する後段経路を含む。厳密な算術は未解明。 |
| [0x00527710](symbols/00527710.md) | func | Input_CheckBattleUiPriority | 戦闘画面で選択・攻撃命令へ進む前に調べるUI優先ゲートの一つ。成立時には他の入力処理が短絡される。 |
| [0x00527EA0](symbols/00527EA0.md) | func | Troop_CleanupCandidateUnits | Troop に関連する選択対象の後処理経路。生存数や Unit+0x8C/+0x1F8 に応じて呼ばれる。 |
| [0x00527ED0](symbols/00527ED0.md) | func | Unit_ResetEmptySelectionState | Unit の候補集合が空の場合に +0x45D を0へ戻し、条件付きで +0x20C も消して後処理を呼ぶ。 |
| [0x00527F60](symbols/00527F60.md) | func | Input_FilterSelectableUnits | Player の選択対象を巡回し、Unit+0x1867C/+0x8C/+0x1F8 などで選択可否を判定する。 |
| [0x00528320](symbols/00528320.md) | func | Input_ClearUnitSelection | Player の既存選択リンクリスト +0x348 と件数 +0x34C を消去する。 |
| [0x00529DC0](symbols/00529DC0.md) | func | GroupList_MergeBucketsForOrder | For list count&gt;=2 creates 26 temporary 12-byte buckets and calls 0x52AD00 at three bounded native merge sites; two distinct callers at 0x5296A8/0x529868; actual game priority/complete tie ordering  |
| [0x005421D0](symbols/005421D0.md) | func | Ai_WriteDistance8AngleSentinel | Original x86 stores two coordinate pairs, computes signed squared-distance/sqrt, and conditionally writes double 10000.0 to context+0x50 after an 8.0 gate. Ordinary finite threshold interpretation onl |
| [0x00542280](symbols/00542280.md) | func | Ai_ReadAngleOrAtan2Fallback | Original x86 returns context+0x50 for ordinary ordered nonsentinel values; exact 10000.0 branches to two signed coordinate deltas, 0x5E743A atan2 and float-rounded pi. ABI and runtime VERIFY; corrects |
| [0x00543E00](symbols/00543E00.md) | func | Unit_DestroyBattleUnit | BattleUnit の破棄処理。Unit+0x1E4B8 にある召喚記録用の木を解放する経路を持つ。 |
| [0x00544290](symbols/00544290.md) | func | Battle_CreateSimpleUnit | SimpleUnit の戦闘用オブジェクトを生成する入口。初期化で Unit+0x8C/0x8D を通常型として設定する。 |
| [0x005445E0](symbols/005445E0.md) | func | SimpleUnit_OnDefeated | 簡易戦闘型 BattleUnit の vtable+0x58（除去）。+0x1867C と UnitData+0x1B1 を立て、HP+0x90=0、element_lost の子を消す。死亡だけでなく撤退でも使われる（実機：原作の簡易戦闘で HP が残ったままの除去が 187 件中 109 件） |
| [0x00544770](symbols/00544770.md) | func | SimpleUnit_Retreat | SimpleUnit の vtable+0x5C。vf+0x58（除去）を呼んでから +0x18680=1 を立てる撤退処理。戦闘差し替えで外部結果の撤退に使い、撤退先・放浪化は原作が処理した |
| [0x00544790](symbols/00544790.md) | func | SimpleUnit_ReceiveDamage | SimpleUnit の vtable+0x70。__thiscall(self, ダメージ, 攻撃者 or NULL, 技能, 0)、ret 0x10。HP+0x90 を引き、0 以下で撃破報酬・生存判定 0x588470→UnitData+0x1B0・vf+0x58・dead_event を行う。技能は NULL 不可。0xF4241 は即死の特別値 |
| [0x005450C0](symbols/005450C0.md) | func | UnitData_ReleaseRecordTree | BattleUnit の記録木を後処理する破棄補助。0x543E00 側から呼ばれ、0x5454D0 に接続する。 |
| [0x005454D0](symbols/005454D0.md) | func | UnitData_ReleaseRecordNode | 記録木の要素を解放する補助。後段で UnitData の文字列・vector 破棄 0x4591F0 へつながる。 |
| [0x00545740](symbols/00545740.md) | func | Unit_UpdateSimpleFrame | SimpleUnit 側の戦闘更新経路。探索カウンタ Unit+0x1E534 を増やし、ノックバック判定より前に行動処理を進める。 |
| [0x00545CC0](symbols/00545CC0.md) | func | Skill_DispatchUnitAbility | Unit の技能種別から行動系統を振り分ける。func の 1=sword、2=missile、3=heal、4=summon を主分岐とする。 |
| [0x00545EC5](symbols/00545EC5.md) | code | Skill_DispatchKindJumpTable | func の種別を4要素の分岐表へ振り分ける位置。5/6はその分岐表の範囲外。 |
| [0x00546F70](symbols/00546F70.md) | func | Skill_ExecuteMissile | missile 技能の処理本体。Skill+0x44 の allfunc が有効なら 0x547DB0 側へ分岐する。 |
| [0x005470FF](symbols/005470FF.md) | code | Skill_UpdateMissileStateField | 通常missile処理で Unit+0x18688 を更新し、Skill+0x2D0==7 の場合だけ旧値に戻す箇所。 |
| [0x00547490](symbols/00547490.md) | func | Summon_ProcessSkillKind4 | Skill+0x40==4 の召喚系 producer の一つ。UnitData の一時コピーと記録挿入に 0x466BA0→0x577310 を用いる。 |
| [0x005479F0](symbols/005479F0.md) | code | Summon_LinkChildCall_Simple | 簡易戦闘の召喚 0x547490（ECX=スキル）内の 0x5774A0 呼び出し。スキルは呼び出し元 [esp+0x18]（呼ばれた側 [esp+0x24]）。 |
| [0x00547AF0](symbols/00547AF0.md) | func | Skill_ExecuteHealAllTargets | heal + allfunc の支援候補を距離・確率などで判定し、対象ごとに 0x551490 を実行する。 |
| [0x00547DB0](symbols/00547DB0.md) | func | Skill_ExecuteMissileAllTargets | missile + allfunc の対象処理経路。従来の未確定扱いは T012§21 で解消された。 |
| [0x0054A170](symbols/0054A170.md) | func | Skill_FilterSupportCandidates | Skill+0xA1C が指定されると支援候補に追加適用される除外フィルタ。フィルタの厳密な条件は未同定。 |
| [0x0054A1C0](symbols/0054A1C0.md) | func | Skill_PrepareLargeCandidateSet | Skill+0xA18 と候補数を受ける補助。4件境界の前処理に関わるが、最終的な順序・件数の意味は未確定。 |
| [0x0054A660](symbols/0054A660.md) | func | Skill_RankCandidateCallback | 24バイト単位の候補集合と Skill+0xA18 由来の第4引数を受ける。候補の選択・整列処理の詳細は未検証。 |
| [0x0054A7B0](symbols/0054A7B0.md) | func | Skill_PrepareHealCandidateGroup | 通常 heal 系の候補前処理で4件を超える場合の補助として使われる。選択結果の意味は未確定。 |
| [0x0054ADA0](symbols/0054ADA0.md) | func | Skill_BuildSupportCandidateList | 支援技能の一時候補リストを作る。Skill+0xA1C による後続除外フィルタより前に呼ばれる。 |
| [0x0054B280](symbols/0054B280.md) | func | Skill_CompareSupportCandidates | Skill+0xA18 の候補比較時に使われる二要素 callback として記録されている。実際の技能結果への到達は未検証。 |
| [0x0054E0B0](symbols/0054E0B0.md) | func | Skill_ExecuteSupportEffect | 支援技能の実行側が参照する補助処理。対象座標から作る方位値を Unit+0x18688 へ書く経路に接続する。 |
| [0x0054E420](symbols/0054E420.md) | func | Skill_UpdateEffectObject | 効果オブジェクトの仮想関数表 +0x04 に置かれる更新処理。生成レコードと GameTask 更新系に接続する。 |
| [0x0054E7B0](symbols/0054E7B0.md) | func | Summon_SpawnFromSkill | 技能・発動元を受けて召喚処理を進める大規模関数。呼出元に Missile/RushMissile などがあり、Unit+0xC の holder 参照を生成先へ渡す。 |
| [0x0054ED95](symbols/0054ED95.md) | code | Summon_SaveSourceUnitOnFlash | 召喚処理で source Unit-like オブジェクトを SummonFlash+0x7C に記録する位置。 |
| [0x0054F074](symbols/0054F074.md) | code | Summon_ReadInheritedHolder | 召喚元の Unit+0xC にある holder を読み、生成 Unit に渡す引数を準備する位置。 |
| [0x0054F245](symbols/0054F245.md) | code | Summon_LinkChildCall | 通常戦闘の召喚 0x54E7B0 内の 0x5774A0(parent, child) 呼び出し。このとき召喚に使ったスキルが呼び出し元の [esp+0x44]（呼ばれた側の [esp+0x50]）にある。スキルのデータの先頭 +0x00 はキー名の std::string。 |
| [0x005501A0](symbols/005501A0.md) | func | Rush_UpdateFrame | Rush の vtable +0x04 に登録された更新処理。GameTask 側の仮想更新ゲートから呼ばれる。 |
| [0x00550D80](symbols/00550D80.md) | func | Damage_ComputeSkillStrength | Skill+0x27C の str mode 1〜5を解釈し、Unit能力値と +0x280/+0x288 の係数から攻撃基礎値を作る。 |
| [0x00550E70](symbols/00550E70.md) | func | Damage_ComputeAttackDefense | 攻撃と防御に別々の乱数を掛け、耐性・距離・最低値の分岐を処理する中核。確認経路ではHP用補正値とEXPへ渡す保持計算値を分ける。実際に減ったHPだけからEXPを再計算する処理ではない。耐性10はゼロ、耐性0は特殊な大値。 |
| [0x005510E5](symbols/005510E5.md) | code | Damage_ZeroOnFullResistance | ダメージ計算中に耐性index10で最終値をゼロにし、通常の最低ダメージ補正を通さない分岐。 |
| [0x00551167](symbols/00551167.md) | code | Damage_ExpAwardCall | 0x550E70内の経験値helper呼出位置。確認経路ではHP変更後、保持した攻撃計算値EDIと対象UnitData+0x178を渡す。実HP減少量へ分子を切り詰めない。actor=[ctx]、skill=[ctx+8]、獲得可否のgateはcallee側。 |
| [0x00551490](symbols/00551490.md) | func | Skill_ApplyHealStatus | 回復・状態変更の共通処理。Skill+0x158のadd2由来リストを参照する経路を持つ。EXPへは上限調整前の計算量を渡す。同一contextを再利用する複数項目処理は、外部resetがなければ項目数ぶんの再加算にはならない。 |
| [0x00551574](symbols/00551574.md) | code | Skill_ReadAdd2RuntimeVector | 回復・状態処理が Skill+0x158 の add2 リストを読み始める位置。 |
| [0x00551C6A](symbols/00551C6A.md) | code | StatusSkill_ExpAwardCall | 0x551490の回復・状態変更経路から経験値helperを呼ぶ位置。元の計算量を渡し、実回復量への差替えではない。同一context再使用時の重複防止gateはcallee側にあり、項目ごとの呼出を獲得回数と同一視しない。 |
| [0x00551E50](symbols/00551E50.md) | func | Hit_LinkedAward | 戦闘中の経験値付与。確認経路ではcontext+0xCの重複防止gateを持つ。heal(kind3)の割合は固定2%で、実回復量への単純比例ではない。対象選別・所属・exp_per等の条件は別に残る。 |
| [0x00551FB2](symbols/00551FB2.md) | code | Hit_LinkedAward_AddExp | 0x551E50 内の経験値加算 add [edi+0x16C],edx（6バイト）。EDI=加算先 UnitData、EDX=量、ESI=context（[esi]=actor）。DLL のフック候補。 |
| [0x00552EF0](symbols/00552EF0.md) | func | Summon_DispatchAlternativeSkill | 0x553390 を呼ぶ種別4の上流分岐。技能種別と後続召喚経路を結ぶ。 |
| [0x00553390](symbols/00553390.md) | func | Summon_ProcessAlternativeKind4 | もう一方の召喚処理 producer。Skill+0x74 の繰り返しや零値fallbackを含み、0x577310 に記録を渡す。 |
| [0x005537BF](symbols/005537BF.md) | code | Summon_LinkChildCall_Missile | 簡易戦闘のミサイル経由の召喚 0x553390（ECX=スキル、親=ミサイル+0x78）内の 0x5774A0 呼び出し。スキルは呼び出し元 [esp+0x2c]（呼ばれた側 [esp+0x38]）。 |
| [0x005559B0](symbols/005559B0.md) | func | Window_HandleWin32Messages | Win32 WndProc。WM_ACTIVATE の状態に応じて 0x879822/0x879823 を切替え、非アクティブ時は入力バッファ処理へ進む。 |
| [0x00555AD0](symbols/00555AD0.md) | func | Startup_LoaderThread | 起動時のデータ読込スレッド（a_system/xp.txt がある場合は同期で実行） |
| [0x00555D69](symbols/00555D69.md) | code | Startup_SetLoadingFlag | g_loadingFlag=1 にする位置 |
| [0x00555E15](symbols/00555E15.md) | code | Startup_ClearLoadingFlag | ローダー終了後に g_loadingFlag=0 にする位置 |
| [0x00555F19](symbols/00555F19.md) | code | Main_MessageLoop | メインスレッドのメッセージループ |
| [0x0055A000](symbols/0055A000.md) | func | Unit_DestroyStaticVariant | 静的ユニット系の破棄処理。共通 BattleUnit 破棄関数 0x543E00 を呼び出す。 |
| [0x0055B010](symbols/0055B010.md) | func | Unit_DeleteStaticVariant | 静的ユニット系の deleting destructor 相当。flag の bit0 が立つ場合にオブジェクト本体も解放する。 |
| [0x0055B030](symbols/0055B030.md) | func | SimpleStaticUnit_Disable | SimpleStaticUnitのvirtual+0x58に対応する無効化処理。保存済み局所報告ではUnit+0x1867Cが非0なら復帰し、0なら1を設定して0x49D9F0、0x4E4F60を呼ぶ。各calleeの全副作用、型/実機動作は未確認。 |
| [0x0055B590](symbols/0055B590.md) | func | StatusWnd_Hide | 詳細パネルを閉じる（StatusWnd 系の仮想関数 vf04） |
| [0x0055B5B0](symbols/0055B5B0.md) | func | StatusWnd_OpenForUnit | 詳細パネル（ボタンあり）をユニットで開く |
| [0x0055BAB0](symbols/0055BAB0.md) | func | TempStatusWnd_OpenForUnit | 一時の詳細パネルをユニットで開く（表示状態 0x80000008 を渡す）。先に閉じる→0x8BCF00設定→組立て0x55BC60を1回→表示。所要は初回のユニット52〜435ms（中央値128）、2回目以降24〜90ms（中央値44） |
| [0x0055BC60](symbols/0055BC60.md) | func | StatusWnd_Layout | 詳細パネルの組み立て（thiscall、引数 char）。表示中に何度も呼ばれる。自勢力でも引数は 0。画像はチップ0x424C80(0x55BD4B)・矩形0x423D70(0x55BDD5)・0x424630(0x55BED9)・顔0x584830(0x55BF3F) |
| [0x0055D712](symbols/0055D712.md) | code | StatusWnd_Layout_ButtonsA | ボタン作成の 1 組目（実機では通らなかった） |
| [0x0055D7FF](symbols/0055D7FF.md) | code | StatusWnd_Layout_ButtonsB | ボタン作成の 2 組目の始まり。noremove_unit など 3 つの設定を引く |
| [0x0055D8F6](symbols/0055D8F6.md) | code | StatusWnd_Layout_ButtonGate | ボタンを作るかどうかの判定の入口（所属先・プレイヤー勢力・出撃準備中） |
| [0x0055D93A](symbols/0055D93A.md) | code | StatusWnd_Layout_MakeHire | 「雇用」ボタンを作る（+0x1C4 を 1 に） |
| [0x0055D95F](symbols/0055D95F.md) | code | StatusWnd_Layout_MakeExtract | 「召上げ」ボタンを作る（陪臣のとき、+0x1C5 を 1 に） |
| [0x0055D99C](symbols/0055D99C.md) | code | StatusWnd_Layout_MakeDismiss | 「解雇」ボタンを作る（+0x1C6 を 1 に） |
| [0x0055D9DD](symbols/0055D9DD.md) | code | StatusWnd_Layout_MakeItem | 「アイテム」ボタンを作る（+0x1C7 を 1 に） |
| [0x0055D9FC](symbols/0055D9FC.md) | code | StatusWnd_Layout_ButtonsEnd | ボタン処理の終わり |
| [0x00560650](symbols/00560650.md) | func | StatusWnd::vf15_shared2 | マウス押下。+0x1BC がなし（0x80000008）で WarWnd 非表示のとき、印 +0x1C4〜+0x1C7 のどれかが立っていれば 3 つの矩形を当たり判定し、その番号の印が立っていれば +0x1BC に番号を入れる。印が全部 0 なら何もせず 0 を返す |
| [0x005606A2](symbols/005606A2.md) | code | StatusWnd_PressWarWndCheck | ボタン押下の処理（vf15）の中で、出撃準備中（WarWnd 表示中）なら押下を受け付けない判定。§93.2 の「ホバー処理」は誤りで、正しくは押下処理 |
| [0x00560CA0](symbols/00560CA0.md) | func | StatusWnd::vf16_shared2 | マウスを離したときの処理。+0x1BC（押下中の番号）が 0x80000008（なし）なら何もしない。それ以外は、印を確認し直さずにその番号の動作（解雇など）を実行する。押下（vf15）は印を確認してから +0x1BC を設定するので、押す前に印を 0 にし +0x1BC を戻せば動作しない |
| [0x00561120](symbols/00561120.md) | func | StatusWnd::vf17 | 詳細パネルの説明表示（マウスを重ねるとスキル説明を出す） |
| [0x00562140](symbols/00562140.md) | func | StatusWnd::vf18_shared2 | 説明表示を消す |
| [0x00565700](symbols/00565700.md) | func | Event_UpdateBattleLimit | 戦闘時間制限の現在カウンタを更新する補助。番兵値のとき増加し、それ以外では正値を減らす。 |
| [0x00565730](symbols/00565730.md) | func | Event_GetBattleLimit | 戦闘時間制限の現在値を返す。state[0x67B938] が番兵なら 0x7FFFFFFF を返す。 |
| [0x00565750](symbols/00565750.md) | func | Event_GetElapsedLimitTime | 時間制限ありなら初期値から現在値を差し引き、番兵状態では現在値を返す。 |
| [0x00567EC0](symbols/00567EC0.md) | func | SortCandidate_CompareSignedField1BC | Original 26-byte callback compares signed 32-bit fields at two pointer arguments +0x1BC and SETL returns 1 iff first&lt;second; two verified sort callsites; exact object type and global sort semantics |
| [0x005681C0](symbols/005681C0.md) | func | T028_RetreatSpotOrFailureString | Original x86 conditional destination search; zero result constructs failure string, nonzero stores Unit+0x1B4 and INC Spot+0xB8 before Unit virtual dispatch. Full ABI, actual retreat and message displ |
| [0x00569360](symbols/00569360.md) | func | TroopFirstEligiblePartnerRatioGate | 最初の適格Unitをアンカーとして他の適格候補の近接比率を判定すると原報告が解析。通常有限値のモデルではM/N&gt;=0.5、比較相手なし等は1。FPU特殊値・ABI・実動作は未確認。 |
| [0x00569530](symbols/00569530.md) | func | Mode30_WriteAndConditionalDispatch | Original x86 writes incoming EAX at owner+0x30 then, for a nonempty member vector, conditionally invokes 0x569730 for the first local +0x1867C==0 member; three verified E8 callers. ABI/gameplay effect |
| [0x005699C0](symbols/005699C0.md) | func | TroopPositionCandidateScratchProducer | 構成員候補を列挙し、局所mode別に配置候補pairを共有scratchへ積む処理候補。原報告は角度候補のowner+0x28保存と8byte単位のscratch再利用を記録。型・座標系・ABI・実出力は未確認。 |
| [0x0056AB20](symbols/0056AB20.md) | func | TroopVirtualSlot4_PeriodicCandidateRoutine | Troopのvtable+4に対応すると原報告が記録する候補処理。入口の条件を通ると局所カウンタを更新し、周期条件付きで0x569360を呼ぶ。実仮想CALL到達・士気や逃走との関係・ABIは未確認。 |
| [0x0056F6F0](symbols/0056F6F0.md) | func | Unit_InitializeRuntimeHolder | Unit の生成時に渡された所有者文脈を Unit+0xC に設定する補助。召喚元 Unit+0xC からの継承経路で使用される。 |
| [0x0056F720](symbols/0056F720.md) | code | Unit_SetHolderField | Unit の生成側でコンストラクタ引数を Unit+0xC に書き込む命令位置。 |
| [0x0056F880](symbols/0056F880.md) | func | Unit_ConstructSummonedRuntime | 召喚時にも使用される通常 Unit オブジェクトの生成処理。owner/holder 引数を 0x56F6F0 へ渡し、vtable 0x63A9E4 を設定する。 |
| [0x00570C90](symbols/00570C90.md) | func | Unit_DeleteNormalVariant | 通常 Unit の vtable 先頭に置かれる破棄関数。0x543E00 から記録木の解放へ進む。 |
| [0x00571A40](symbols/00571A40.md) | func | Ai_CheckOrientationGate | AI の方位差判定に先行して戻り値 AL が使用される補助。AL の詳しい意味は未確定。 |
| [0x00571B70](symbols/00571B70.md) | func | Unit_InitializeBattleInstance | キャンペーン側の参照 Unit から戦闘インスタンスへ状態を引き継ぐ際に呼ばれる。技能の種別別能力フラグ再構築とも関連する。 |
| [0x00573BD0](symbols/00573BD0.md) | func | Unit_CopyStatsFromDef | def の能力値を Unit オブジェクト（+0x90..）へ展開し、*_max を作る |
| [0x00574D70](symbols/00574D70.md) | func | BattleCandidate_ScriptListInsertNode | World Script側callerからUnit+0x18654の候補countを1増加しnode連結。unsigned capacity guardは正常count前提の条件付きであり具体的なDAT command・実標的は未確定。 |
| [0x00574E30](symbols/00574E30.md) | func | BattleCandidate_ScriptListEraseMatchingNode | Unit候補listで一致nodeをunlink/freeして+0x18654を減少させる局所処理。別vector消去とscript実命令意味はVERIFY。 |
| [0x00575110](symbols/00575110.md) | func | Unit_LevelUpLoop | Unit 版のレベルアップ |
| [0x00575A60](symbols/00575A60.md) | func | Unit_OnDefeated | 通常型 BattleUnit の vtable+0x58。最初の1回だけ +0x1867C を立て、生きている子のうち element_lost の子を子の vtable+0x58 で消す。陣営 +0x48 の一覧からは外さない。 撤退でも使われる除去処理と見られる（SimpleUnit 版の実機結果から。通常型は未確認） |
| [0x005769B0](symbols/005769B0.md) | func | Unit_ProcessKnockbackMotion | ノックバック関連の Unit+0x18688 などを更新する関数。押し戻し移動と状態値の複数分岐を含む。 |
| [0x00576F10](symbols/00576F10.md) | func | SkillFlash_PostDamage_GatedRingDispatch | Bounded original x86: Unit+0x1867C/+0x8D gates, 8-slot R ring Unit+0x928+idx*0x264, conditional direct 0x4DFBB0 call, normal ret 4; lower effect/RNG unverified |
| [0x00577100](symbols/00577100.md) | func | Unit_PostHpTierRegister | Original x86 288B/85 instructions: Unit flag guards; mode0 0x41E160 unlink and timer clear; enabled HP/HPmax/0.05 integerized tier clamp 0..20 to +0x738; conditional 0x41E060 registration; +0x185F4=15 |
| [0x00577260](symbols/00577260.md) | func | UnitData_FindSummonRecord | BattleUnit 所有の文字列キーの木から記録 R を検索し、見つからなければ0を返す。呼出規約は ECX=owner、スタックの28バイトキー引数を関数側で回収する。 |
| [0x00577310](symbols/00577310.md) | func | UnitData_InsertSummonRecord | BattleUnit の記録木へ大きな値引数を挿入する。呼出前には約0x1D4バイトの引数領域を作り、戻り値はRへのポインタ。 |
| [0x00577405](symbols/00577405.md) | code | UnitData_ReturnInsertedRecord | 召喚記録の挿入関数が EAX に記録 R のポインタを返す位置。 |
| [0x005774A0](symbols/005774A0.md) | func | Unit_AppendSummonChild | 親 BattleUnit の子一覧 +0x178/+0x17C/+0x180 に子を追加する（stdcall(parent, child) ret 8）。子の +0x1E594 が 0 でなければ親に書き換える。呼出しは召喚生成直後の 0x54F245/0x5479F0/0x5537BF の3か所のみ。一覧から外す処理はない。 |
| [0x00577600](symbols/00577600.md) | func | BattleCandidate_CountGatedStatusUpdate | Unit+0x18654が零の分岐と、非零時の候補条件によるUnit+0x18638/3C局所更新を持つ。最終ゲーム効果とABIは未検証。 |
| [0x00578370](symbols/00578370.md) | func | Unit_ReceiveDamage | 通常 Unit の vtable+0x70（表の項目 0x63AA54）。SimpleUnit_ReceiveDamage と同じ形で、dead_event_a/d と 0x4321B0 呼出しを含む。直接 E8 の呼出し元は無い |
| [0x00578B70](symbols/00578B70.md) | func | Status_ApplyGaugeReduction | 状態異常ゲージを減算し、unit_status_min を下限として制限する。EXP吸収分岐もこの関数内にある。 |
| [0x00579940](symbols/00579940.md) | func | UnitData_CompareRecordKeys | 記録木の文字列キーを短文字列とヒープ文字列の双方から読み、辞書順に比較する処理を含む。 |
| [0x00579EB0](symbols/00579EB0.md) | func | BattleCandidate_MergeBucketLists | 候補listから一時carryと26桶へ移管・mergeし、最後に入力listへ戻す原作x86経路。攻撃先の確定処理ではない。 |
| [0x0057A6E0](symbols/0057A6E0.md) | func | UnitData_CreateRecordNode | 記録木で512バイトのノードを確保し、node+0x28 に UnitData 相当の記録本体を構築する。 |
| [0x0057A764](symbols/0057A764.md) | code | UnitData_AdvanceToPayload | 記録ノードのキー文字列領域を0x1Cバイト進め、record本体のコピー先を準備する位置。 |
| [0x0057A7D0](symbols/0057A7D0.md) | func | BattleCandidate_WritePerNodeRngScoreOffset | Unit候補listを各node反復し原作randとfloat変換後、候補+0xA14へ-4-EAX補正を書込む。正確な乱数実行順・最終標的は未検証。 |
| [0x0057A830](symbols/0057A830.md) | func | List_MergeWithNativeComparator | 2 listの先頭candidateを比較子0x5A3EA0へ渡し単nodeと残余を0x4C5800へspliceする。汎用ABIと異常系は未検証。 |
| [0x0057AA00](symbols/0057AA00.md) | func | Unit_UpdateBattleFrame | もう一方の Unit 戦闘更新経路。探索カウンタを加算し、0x57ABB2 付近でノックバック状態を判定する。 |
| [0x0057B870](symbols/0057B870.md) | func | Ai_SearchTargetCadence | 探索閾値に届かない間は既存ターゲットを使い、到達後は候補探索してカウンタを約±10%の乱数付きで再設定する。 |
| [0x0057BE30](symbols/0057BE30.md) | func | Skill_PostActionUpdate | ECXに技能参照・stackにUnit参照を受け、技能後段でUnit待機フィールド・キー付き管理値・条件付き通知ラッチを更新する局所処理。正常末尾0x57C170はret4。下位関数の作用と実機挙動は未検証。 |
| [0x0057C9B0](symbols/0057C9B0.md) | func | Ai_CheckFacingSelection | 行動対象の方位差に関係する検査を含み、Unit+0x186C8 が番兵値のとき一部の方位判定を回避する。 |
| [0x0057CFA0](symbols/0057CFA0.md) | func | Ai_CopySupportTargetCache | 支援対象の候補レコードを Unit 側キャッシュにコピーする補助。候補の優先順位そのものを決める本体ではない。 |
| [0x0057CFD0](symbols/0057CFD0.md) | func | Ai_MergeSupportTargetCache | 支援技能の候補ベクトルを Unit 側へ結合する補助。最終技能選択とは区別する。 |
| [0x0057D1D0](symbols/0057D1D0.md) | func | Ai_UpdateSpatialTargetLink | Unit+0x1E594 にある別 Unit 参照が有効なら、両者の +0x220/+0x224 座標差を計算する処理に進む。 |
| [0x0057D8B0](symbols/0057D8B0.md) | func | Ai_AdjustSearchTargetCoordinates | 目標探索の後段で現在時刻や戦場境界を参照して座標候補を補正する関数。補正の全条件は未確認。 |
| [0x0057DD10](symbols/0057DD10.md) | func | BattleCandidate_HeadSentinelOrPairBranch | 候補countと先頭候補の+0x40/+0x26D条件を検査してUnit+0x186C8/CCに番兵または局所2値を書き分ける経路。実攻撃対象を確定した証拠ではない。 |
| [0x0057DF90](symbols/0057DF90.md) | func | Status_ApplyNaturalRecovery | 行動カウントに連動して HP/MP と7つの状態ゲージを回復し、unit_status_hp をゲージ上限にする。 |
| [0x0057E1D0](symbols/0057E1D0.md) | func | Unit_ExecuteActionRoute | Unit の戦闘行動処理経路の一つ。ダメージ計算 0x550E70 への呼び出し元を含む。 |
| [0x0057E4E0](symbols/0057E4E0.md) | func | Unit_RefreshActionSearch | Unit+0x1E534 を探索閾値にして 0x57B870 を呼び、ターゲット再探索を強制する経路を持つ。 |
| [0x0057EB40](symbols/0057EB40.md) | func | Unit_DispatchBattleAction | 探索更新後の行動候補を処理し、ALを上位分岐に使う。保存済み著者報告では射撃ラッチ2を設定してAL=0で早期returnし、後続MP減算へ進まない経路がある。ALだけを攻撃成功/失敗へ一律対応させない。mode0/1のcaller経路は別。 |
| [0x0057F570](symbols/0057F570.md) | func | Skill_EvaluateSupportCandidate | 支援技能の候補キャッシュを参照し、空なら失敗を返す。MPと射程による後段フィルタに接続する。 |
| [0x0057FC90](symbols/0057FC90.md) | func | Skill_EvaluateSupportAlternative | 支援候補キャッシュを用いる別の技能実行経路。候補が空なら早期失敗し、射程・MPなどを再評価する。 |
| [0x0057FFD0](symbols/0057FFD0.md) | func | Skill_ExecuteAllfuncKind2 | kind2 技能で allfunc が指定された場合の候補ループと乱数・MP境界を扱う。通常AIの直接技能選択とは別段階。 |
| [0x00580280](symbols/00580280.md) | func | Skill_ExecuteLinkedEffect | 技能リストのリンク先を処理し、Skill+0x74 と +0xF4 に応じて別実行経路を選ぶ。MP消費判定を含む。 |
| [0x00582D90](symbols/00582D90.md) | func | UnitDef_Create | ユニット定義（def）の生成 |
| [0x00583A80](symbols/00583A80.md) | func | UnitDef_Predicate_583A80 | 放浪先の選定などで使う def の判定（意味は未確定） |
| [0x00583CF0](symbols/00583CF0.md) | func | UnitDef_GetAffiliation | ユニットがいる場所を返す。放浪中（+0x94≠0）なら放浪先 +0x84 を 0x467E90 で引き、そうでなければ ctx+0x2F0 の一覧から探す（後半は疑似コードからの推定）。同じ勢力でもユニットごとに値が違った |
| [0x00583DC0](symbols/00583DC0.md) | func | UnitDef_FindLeaderOfVassal | ユニット定義の一覧をたどり、陪臣の主の人材を探す（推定） |
| [0x005846A0](symbols/005846A0.md) | func | UnitDef_GetDisplayName | 表示名を作る。ECX=def、EDX=std::string* out |
| [0x00584830](symbols/00584830.md) | func | UnitDef_GetFaceBitmap | thiscall ECX=ユニット定義、引数なし、素のret、EAX=HBITMAPか0。"face"を0x585AD0で引き0x4243C0へ。無ければ兵種のface。1回約5ms |
| [0x00584970](symbols/00584970.md) | func | UnitDef_GetChipName | キャラチップ名を決める（image / sub_image / tkool を考慮）。thiscall: ECX=def、引数 (std::string* out, flag=1)、ret 8 |
| [0x00585AD0](symbols/00585AD0.md) | func | UnitDef_GetField | ユニット定義の DAT プロパティ（"level"、"noremove_unit" など）を、ユニット ID とクラスをたどって引く |
| [0x00586320](symbols/00586320.md) | func | UnitDef_GetFriendSet | friend 集合の遅延生成（def+0x158） |
| [0x00587CC0](symbols/00587CC0.md) | func | Unit_CachedValueOrAggregate | T011§17では引数0はUnit+0x1C4のキャッシュ返却。非0は重み付き入力集計の先頭区間までの確認で、最終返値・内部書込・全体副作用は同区間では未証明。Fの格納・返値利用の実装報告との原作帰属照合は未実施。 |
| [0x00588470](symbols/00588470.md) | func | Unit_DeathSurvivalRoll | 戦死時の生存判定と見られる（P0 exit 研究：EXP 補正、関連記録+0x174 または勢力+0x5C 減算、alive_per の乱数）。戻り値 AL を UnitData+0x1B0 に書く（0x578975、0x544B50）。旧名 UnitData_ResolveTypedDefinition は根拠が薄いので訂正 |
| [0x0058A400](symbols/0058A400.md) | func | UnitDef_ExpNext | 次のレベルに必要な経験値の計算（符号なし） |
| [0x0058A540](symbols/0058A540.md) | func | UnitDef_ExpTotal | 経験値の累計計算（符号付き） |
| [0x0058A650](symbols/0058A650.md) | func | UnitDef_LevelUpLoop | def 単体のレベルアップのループ |
| [0x0058AFA0](symbols/0058AFA0.md) | func | UnitDef_ApplyClassSkills | class 変更・learn・delskill2 の技能処理 |
| [0x0058B7F0](symbols/0058B7F0.md) | func | UnitDef_ComputeStats | def に能力値（基本値＋成長×(Lv-1)、上限あり）を書く |
| [0x0058C0E0](symbols/0058C0E0.md) | func | UnitDef_BuildSkillList | def の技能リスト（def+0xEC）を作る |
| [0x0058DA40](symbols/0058DA40.md) | func | UnitDef_SkillListPostProcess | 技能リストの後処理 |
| [0x0058E870](symbols/0058E870.md) | func | Save_ReadUnitDataRecord | 通常ロードで Unit レコード 1 件を読む。書出し 0x58EFD0 と対 |
| [0x0058EFD0](symbols/0058EFD0.md) | func | Save_WriteUnitDataRecord | 通常セーブの UnitData の各数値フィールドを個別に出力するシリアライザ。engine+0x300 グループから参照される。 |
| [0x0058F7E0](symbols/0058F7E0.md) | func | Variable_EraseOldMappedValue | 数値変数の既存record更新時の一部条件で呼ばれる、旧値処理の補助。厳密な破棄条件は未確認。 |
| [0x00593890](symbols/00593890.md) | func | Power_Personality | 勢力の性格 |
| [0x00595320](symbols/00595320.md) | func | Training_GetEffectiveUpCount | Power+0xD8が非零ならそれを用い、零ならscenario.training_upを参照する訓練基礎回数取得。x86の零→1・負→0正規化を含む。0x472081から呼ばれる。実機結果は未照合。 |
| [0x005964C0](symbols/005964C0.md) | func | Save_ReadPowerGroupRecord | 通常ロードで Power レコード 1 件を読む。書出し 0x596AA0 と対 |
| [0x00596AA0](symbols/00596AA0.md) | func | Save_WritePowerGroupRecord | 通常セーブの Power レコードを書く（名前、+0x1C、+0x1D、資金、盟主、+0x40、性格、+0x60、+0x74、領地、merce、staff、表 +0xB4、札 fixtype〜base_level、home_spot、空文字 2 つ）。表 +0xB4 は区切りなしで札 fixtype で終わる。 |
| [0x005972E0](symbols/005972E0.md) | func | Spot_LoadRuntimeCapacity | Spot の capacity を読み、未指定0なら scenario のspot_capacityを代用し、最終値を最大24に制限する。 |
| [0x005973AF](symbols/005973AF.md) | code | Spot_ApplyCapacityFallback | Spot 読込時に固有 capacity が0なら scenario 側の容量値を採用する分岐。 |
| [0x00597412](symbols/00597412.md) | code | Spot_ClampCapacityTo24 | Spot 容量の最終値を最大24へ制限する付近の位置。 |
| [0x00597960](symbols/00597960.md) | func | Spot_GetDisplayName | 領地と出力文字列をスタックで受け取りret 8。現在の文脈のspot/nameを取得。原作呼出側で天竜川上流域と一致。改名・DLLからの呼出は未確認。 |
| [0x00597A50](symbols/00597A50.md) | func | T028_FilteredLinkedNodeCount | Original x86 traverses linked nodes; only resolved nonnull nodes with byte+0x78 nonzero increment local count, also used in a signed strict Spot-like capacity gate. Exact object type, overflow and run |
| [0x00597B00](symbols/00597B00.md) | func | Affiliation_GetPower | 所属先から勢力オブジェクトを返す。返り値の +0x1D がプレイヤー勢力の印 |
| [0x00598450](symbols/00598450.md) | func | T028_VectorIndexCleanupFlagBranch | Original x86 366B helper runs pre-flag lookup/erase calls at 0x598469/47C and per-entry 0x5984C7/4DA; flag0 skips extra resolver/destructor paths but not prior tree erase. Object type and runtime outc |
| [0x005985C0](symbols/005985C0.md) | func | World_RebuildSingleSpotSkin | worldskin 再構築で個々の Spot に対して呼ばれる補助。結果が派生グリッド・描画キャッシュの再生成に使われる。 |
| [0x00598980](symbols/00598980.md) | func | Save_ReadSpotGroupRecord | 通常ロードで Spot レコード 1 件を読む。書出し 0x598CE0 と対 |
| [0x00598CE0](symbols/00598CE0.md) | func | Save_WriteSpotGroupRecord | 通常セーブの Spot レコードを書く（名前、map、+0x64、gain、castle、部隊の集合、札 capacity・castlebattle・fightvalue・dunname、空文字）。部隊の集合の後に区切りはなく札 capacity で終わる。 |
| [0x0059C3B5](symbols/0059C3B5.md) | code | Skill_StoreNextOrderParsedFlag | Original x86 writes boolean AL for raw next_order==on to compiled Skill +0x270. Full runtime selection and RNG VERIFY. |
| [0x0059C418](symbols/0059C418.md) | code | Skill_StoreNextIntervalParsedValue | Original x86 writes property getter integer [EAX+0x20] for next_interval to compiled Skill +0x274. Time unit and runtime consumers VERIFY. |
| [0x005A3DF0](symbols/005A3DF0.md) | func | BattleCandidate_ConstructTempRecord | Unitに紐付く一時recordを組み立て、原作RNG由来値をrecord+0x28へ書く。値の実target決定への寄与は未証明。 |
| [0x005A3EA0](symbols/005A3EA0.md) | func | BattleCandidate_CompareModeScoreAndSecondary | mode2は候補+0xA0C、それ以外は+0xA10を基準に追加優先条件を比較。record+0x28直接参照なし。ゲームでの意味は未確認。 |
| [0x005A4100](symbols/005A4100.md) | func | WarWnd_StaticInit | WarWnd の起動時の初期化（名前 'war' を設定） |
| [0x005A8740](symbols/005A8740.md) | func | Spot_ShowRuntimeObject | Spot の vtable+0x54 にある表示処理。Spot+0x88 を1にし、世界画面の表示用オブジェクトを再登録する。 |
| [0x005A89A0](symbols/005A89A0.md) | func | Spot_HideRuntimeObject | Spot の vtable+0x58 にある非表示処理。Spot+0x88 を0にし、描画用オブジェクトを登録集合から外す。 |
| [0x005A9CC0](symbols/005A9CC0.md) | func | T028_PreReg_ThreeHelperDispatch | Original PE 178B function directly E8-calls 0x4C22B0, 0x4C3E40, 0x4BC9C0; full object/geometry meanings VERIFY |
| [0x005AA130](symbols/005AA130.md) | func | T028_ModeTable_RegistrationGate | Original x86 has mode0..11 indirect switch, initial +0x5C/+0x7C/+0x78 stores, +0x74 conditional registration guard; effect gameplay VERIFY |
| [0x005AA6E0](symbols/005AA6E0.md) | func | ResultFlag_StoreAndConditionalPrecall | Bounded original x86 stores AL in receiver+0x8C and conditionally calls 0x5A9CC0 when AL nonzero; gameplay purpose and receiver type VERIFY |
| [0x005AAEC0](symbols/005AAEC0.md) | func | Spot_Search | スポットの探索 |
| [0x005B0400](symbols/005B0400.md) | func | Save_ReadSpotPathPayload | SpotPath と SpotEscapePath が共用する仮想slot +0x5C の保存データ読込関数。 |
| [0x005B0600](symbols/005B0600.md) | func | Save_WriteSpotPathPayload | SpotPath と SpotEscapePath が共用する仮想slot +0x60 の保存データ書込関数。 |
| [0x005B47B0](symbols/005B47B0.md) | func | World_RebuildSpotSkinCache | worldskin 命令の再構築本体。world-base+0x2F0 の Spot 集合を走査して領地の派生表示・空間データを作り直す。 |
| [0x005B5010](symbols/005B5010.md) | func | World_RefreshDerivedSkin | 領地集合を基にした worldskin 再生成の後段で呼ばれる処理。正確な表示キャッシュの項目名は未確認。 |
| [0x005B6BBB](symbols/005B6BBB.md) | func | operator_delete | CRT の operator delete（DLL から解放に使う） |
| [0x005B6E99](symbols/005B6E99.md) | func | srand | CRT の srand |
| [0x005B6EAB](symbols/005B6EAB.md) | func | rand | CRT の rand |
| [0x005B797C](symbols/005B797C.md) | func | CRT_ftell_SEH4_entry | Ogg標準FILEのtellに登録される91 byteのMSVC SEH4付きftell入口。NULL FILE*ではerrno=22とinvalid-parameter handler経路、正常FILE*ではlock→__ftell_nolock→unlock。例外時動作/独立DLL ABIは未検証 |
| [0x005B79D7](symbols/005B79D7.md) | func | CRT_ftell_shared_EBP_unlock_helper | 0x5B79C9から呼ばれる10 byteのunlock補助。親ftellのEBP+8を読むため独立hook呼出ABIを想定しない。0x641260のSEH4 cleanup handler候補にも登録 |
| [0x005BB6E0](symbols/005BB6E0.md) | func | CRT_except_handler4_search_unwind | MSVC __except_handler4。exception flagsでsearchとunwindを分け、filter=0のscopeは検索時にfilter呼出を飛ばす。実ランタイムの対象ftell例外配送とunlock実行保証は未実測 |
| [0x005C3500](symbols/005C3500.md) | func | CRT_LocalUnwind4 | 4経路のE8呼出先として報告されたMSVC局所unwind処理。scope cursor更新・通知副作用はV9推定を含み、完全ABI・実例外での解放は未確認。 |
| [0x005C35BD](symbols/005C35BD.md) | code | CRT_LocalUnwind4_Callsite_PEFragment | 0x5C3590のPE code fragment内と報告されたE8 site。callerの独立関数ABIは未確定。 呼出先は0x5C3500。 |
| [0x005C35E6](symbols/005C35E6.md) | code | CRT_LocalUnwind4_Callsite_5C35D6 | 0x5C35D6のcaller内と報告されたE8 site。callerの独立関数ABIは未確定。 呼出先は0x5C3500。 |
| [0x005C3646](symbols/005C3646.md) | code | CRT_LocalUnwind4_Callsite_ExceptUnwind | 0x5C363B内のE8 site。先行20Hにも記載済みで、新しい独立経路の発見とは数えない。 呼出先は0x5C3500。 |
| [0x005CF970](symbols/005CF970.md) | func | Vorbis_State3InitFromImplicitESI | Original native reads decoder state from ESI+0x58, conditionally initializes state3 via 0x5D5BD0 and writes state4. Early direct caller 0x5D0B8A supplements the pre-existing cached 0x5D0D67 call; full |
| [0x005CFA10](symbols/005CFA10.md) | func | OggPageUpdateLocalStateWriter | 原報告が列挙した自身の直接state書込はowner+0x58への4・EDI(ABI保存を前提に2)・3。callee・alias・再入・他スレッドによる間接変更は未確認。全プログラムの状態不変性や正常EOFを証明しない。 |
| [0x005CFDD0](symbols/005CFDD0.md) | func | Ogg_SeekCallbackLow32Boundary | 標準FILE seek callbackの34byte窓。著者の16H原報告は0x5CFDE8で_fseek側へFILE*/low32/originを渡し、この窓のhigh32読込なしを報告。原報告は今回回収済み。完全ABI・他callback・大容量ファイルの実故障は未確認。 |
| [0x005CFF10](symbols/005CFF10.md) | func | OggAggregateLinkLengthGetter | 原報告ではindex=-1時にリンクの64bit長を合算するgetter。安定したstate&gt;=2・リンクmode・件数条件と無効時-131を分ける。正常EOFで-131になるとは断定せず、破損・再入・overflow等は未確認。 |
| [0x005D0B8A](symbols/005D0B8A.md) | code | Vorbis_State3EarlyInitCallsite | Original E8 direct call to 0x5CF970 after nonnegative upstream 0x5D04E0 return; ESI previously loaded from outer decoder pointer. Different from cached 0x5D0D67 call; only bounded static branch establ |
| [0x005D16C0](symbols/005D16C0.md) | func | OggFileWrapper_OpenWithCloseCallback | 標準ファイル開閉経路でCRT _fclose候補をcallbackとして後続へ渡しouter+0x2C8へ保存させる。別caller/再入は未確認。 |
| [0x005D1B80](symbols/005D1B80.md) | func | ftol | x87 の浮動小数点→整数変換 |
| [0x005D1D33](symbols/005D1D33.md) | code | CRT_LocalUnwind4_Callsite_Fsopen | __fsopen(0x5D1CB1)内のE8 site。空ファイル名のエラー経路との対応はV9擬似Cの推定で、native条件・FILE所有権は未確認。 呼出先は0x5C3500。 |
| [0x005D3D00](symbols/005D3D00.md) | func | VorbisComment_FreeAndReset | コメント配列の非NULL要素をsigned countまで解放し、配列/vendor解放後に4つの管理fieldをゼロ化する。部分構築や二重呼出の異常系は未検証。 |
| [0x005D3DA0](symbols/005D3DA0.md) | func | VorbisSetup_InitInnerState | Original 50-byte helper clears selected outer fields and stores calloc(1,0xE50) result at outer+0x1C; parser null gate is separate and full ABI VERIFY. |
| [0x005D3F60](symbols/005D3F60.md) | func | VorbisHeader_Type1Parse | identification headerのversion・block境界・framing条件を検査し成功時outer+8を正値にする原作x86経路。実機入力異常は未検証。 |
| [0x005D4030](symbols/005D4030.md) | func | VorbisComment_Type3_Parse | Ogg/Vorbis type3コメントヘッダのvendor文字列とコメント配列を確保・読取する経路。原作x86ではcalloc後のNULL未検査書込候補があり、OOM実機挙動と上位エラー伝播は未検証。 |
| [0x005D4160](symbols/005D4160.md) | func | VorbisSetup_WriteTagArrays | 3種setup tag群の個数と値域を検査しtag/pointer配列を初期化する原作x86。別writerや破損入力は未検証。 |
| [0x005D4420](symbols/005D4420.md) | func | VorbisHeader_Type1SignaturePrecheck | 先頭type1と6byte vorbis署名を事前照合する局所原作x86関数。他のpacket種別ルータとは別。 |
| [0x005D44C0](symbols/005D44C0.md) | func | VorbisHeader_TypeOrderRouter | 署名とtype1/3/5を照合し各parse関数へdispatchする。失敗コード-132/-133と種別前提は局所確認で親への伝播は未検証。 |
| [0x005D48E0](symbols/005D48E0.md) | func | OggSeekPositionShiftGetter | 原報告の17byte静的窓では[[EAX+0x1C]+0xE48]の値を返す読取getter。callerは戻り値を位置換算のshift countへ渡す。状態resetという旧解釈は採用しない。単位・値域・実動作は未確認。 |
| [0x005D4900](symbols/005D4900.md) | func | VorbisBitbuffer_CreateFifteenSlots | 親内の埋込index7と個別calloc14件でbitbuffer slot群を初期化。malloc失敗や実ゲーム破損は未観測。 |
| [0x005D4980](symbols/005D4980.md) | func | VorbisGrow_AlignAndAllocateBuffer | 8byte整列要求をsigned容量条件で判定し、必要なら旧使用量+0x50を蓄積してmalloc退避nodeと新bufferを確保。失敗時の実際の到達性はVERIFY。 |
| [0x005D49F0](symbols/005D49F0.md) | func | VorbisGrow_FreeListAndOptionalRealloc | outer+0x54の旧buffer退避listを解放し、+0x50非零のときrealloc結果を+0x44へ未検査上書きする。正の要求での失敗時の参照喪失は条件付きで実機未検証。 |
| [0x005D4A60](symbols/005D4A60.md) | func | VorbisBitbuffer_TeardownFifteenSlots | outer+0x68をガード後に15 slotを解放しindex7だけ個別slot freeを省略。slot自体のNULLガードは未確認。 |
| [0x005D4AE0](symbols/005D4AE0.md) | func | VorbisOuter_CleanupManagedArrays | outerの管理配列を解放しゼロ化する。outer+8がNULLならouter+0xC配列の解放も飛ぶ局所分岐、部分状態到達性は未証明。 |
| [0x005D4D20](symbols/005D4D20.md) | func | VorbisHeader_PostInitializePointerGates | outer+0x68とouter+4と参照先+0x1CのNULLを検査し、欠損は-1・局所成功は0を返す。親に戻り値が伝播するとは限らない。 |
| [0x005D5BD0](symbols/005D5BD0.md) | func | VorbisHeader_InitializeWrapperReturn | 0x5D57C0の非0結果はcleanup後1を返し、0ならpostinit0x5D4D20を呼んで結果破棄し0を返す。正常到達性はVERIFY。 |
| [0x005D9E70](symbols/005D9E70.md) | func | VorbisCodebook_FreeOwnedFields | codebook marker+0x24の分岐で+0x20/+0x08の非NULL所有領域を解放し管理fieldと本体を解放する。割当失敗時の書込保護や別名の安全性は未検証。 |
| [0x005D9F40](symbols/005D9F40.md) | func | VorbisLook_InitBorrowedCodebook | 0x38-byte look recordの+0x0Cに元codebook参照を保存する初期化経路。所有権は局所命令から推定。 |
| [0x005DA070](symbols/005DA070.md) | func | VorbisLook_ConvertRecord | look recordをmemset(0x38)で初期化して変換する経路。初期確保にNULL検査、後続4確保の局所guardは未確認。実機の失敗挙動は未測定。 |
| [0x005DA550](symbols/005DA550.md) | func | VorbisCodebook_ParseWidthBound | codebookのdimension/entry数、bit長合計&lt;=24を判定する静的x86入口。calloc結果の局所NULL未検査があるが実ゲーム異常は未確認。 |
| [0x005DA930](symbols/005DA930.md) | func | Vorbis_CodebookDecode | Vorbis のコードブック復号（ビット検索）。原因不明のクラッシュ 0x5DA9F8 はこの中 |
| [0x005DA9F8](symbols/005DA9F8.md) | code | Crash_5DA9F8 | 汎用UI 試験中に 1 回起きたアクセス違反の位置。原因未特定 |
| [0x005DFE10](symbols/005DFE10.md) | func | VorbisResidue_Parse | residue分類数/次元数と反復積を検査するparser。正常reader/成功受理・未改変条件でB&gt;=1,D&gt;=1,P&lt;=Eの制約を持ち、6bit EOFは次8bit負値拒否へ伝播するという著者報告。 正常reader/非負packet長/未改変成功recordに限定。全alias/入力/ABI/allocator failure/実機挙動を証明しない。 |
| [0x005DFFC0](symbols/005DFFC0.md) | func | VorbisResidue_Init | compiled codebook entryからdimensionを取りresidue instanceへ対応づけ、正常未改変受理条件ではB^Dと確保要求/除数に上限・非ゼロの制約があるという著者報告。 03H局所懸念を04H条件付き訂正と併記。任意object/全入口/allocator failure安全を確定しない。 |
| [0x005E06C0](symbols/005E06C0.md) | func | VorbisGrowCaller_ConditionalBufferWriter | 0x5E072Aで0x5D4980に確保を依頼し戻り値をstackに保持、別の数値条件を通るとポインタ加算後に書く。allocator失敗と零除算の実到達性は未検証。 |
| [0x005E0DC0](symbols/005E0DC0.md) | func | VorbisResidue2_Decode | type2復号関数と報告された入口。instance+0x10のcompiled codebook先頭DWORDを除数として局所IDIVで使用する。 局所division経路だけ。fulldecoder ABI・全副作用・ゲームtype2使用・全除算安全を意味しない。 |
| [0x005E3B70](symbols/005E3B70.md) | func | Ai_ComputeCandidateDistance | 候補選定で座標差の平方和を受ける平方根相当の距離計算補助として呼ばれる。 |
| [0x005E6C70](symbols/005E6C70.md) | func | VorbisBitbuffer_InitializeSlotAndBuffer | slot本体へ0を初期化し内部256Bを確保して先頭書込。確保失敗の局所NULLガードは未確認で実故障は未実証。 |
| [0x005E6CA0](symbols/005E6CA0.md) | func | VorbisBitbuffer_FreeAndClearSlot | slot+8内部bufferをNULL判定し必要ならfree後slot本体0x14を初期化。slot pointer自身を最初に検査しない。 |
| [0x005E6CD0](symbols/005E6CD0.md) | func | VorbisBitreader_Initialize | 20byte readerのbyte cursor/bitOffsetを0にし、packet data pointerとbyte lengthを保存する初期化経路。ABIや異常入力は未確認。 |
| [0x005E6E10](symbols/005E6E10.md) | func | VorbisBitreader_ReadBitsOrEOF | 要求bit幅上限32と残容量を検査して読込み、EOFでcursor/bitOffset/ptrを更新し-1を返す原作x86。上位結果はVERIFY。 |
| [0x005E6F10](symbols/005E6F10.md) | func | VorbisBitreader_ConsumedBytesRoundedUp | byteCursor+ceil(bitOffset/8)を計算する補助。EOF後はtotal+1となり得るが呼出側の異常挙動は未証明。 |
| [0x00626D5C](symbols/00626D5C.md) | string | str_face | "face"。0x584830が顔画像名の取得に使う |
| [0x006385BC](symbols/006385BC.md) | object | vt_SpotDisplayObject | Spot 表示用クラスの仮想関数表。+0x54 が 0x5A8740、+0x58 が 0x5A89A0 に対応する。 |
| [0x00639C5C](symbols/00639C5C.md) | global | vt_StatusWnd | StatusWnd の仮想関数表。+0x44=説明表示 0x561120 |
| [0x00639CD4](symbols/00639CD4.md) | global | vt_TempStatusWnd | TempStatusWnd の仮想関数表。+0x3C=押下 0x560650、+0x40=離す 0x560CA0、+0x44=説明表示（空の関数 0x406E20） |
| [0x0063A4BC](symbols/0063A4BC.md) | object | vt_SimpleUnit | SimpleUnit の仮想関数表。コンストラクタが Unit+0x8C に0x0001を書き、通常ユニット種別となる。 |
| [0x0063A8E4](symbols/0063A8E4.md) | object | vt_SimpleStaticUnit | SimpleStaticUnit の仮想関数表。コンストラクタが Unit+0x8C に0x0101を書き、静的ユニット候補群へ登録する。 |
| [0x0063A9E4](symbols/0063A9E4.md) | object | vt_UnitRuntime | 通常型 Unit の仮想関数表。0x56F880 の生成時に vptr へ書き込まれる。 |
| [0x0063B058](symbols/0063B058.md) | global | g_IntervalQuantum | isInterval が指定間隔を切り上げる際の定数double 10.0。 |
| [0x0063B060](symbols/0063B060.md) | global | g_RandomPercentScale | 候補のstealth判定で0〜99の乱数を作る際に掛けるdouble 100.0。 |
| [0x0063B070](symbols/0063B070.md) | global | g_PercentToRatioFactor | 整数パーセントを倍率にする定数double 0.01。damage_consti 読込時などに使われる。 |
| [0x0063B080](symbols/0063B080.md) | global | g_RandomUnitScale | CRT rand の整数を0〜1相当へ換算するdouble 1/32768。stealth確率と鍵生成などに使われる。 |
| [0x0063B100](symbols/0063B100.md) | global | g_SaveKeyRandomSpan | 保存エンベロープの鍵バイト生成で使うdouble 112.0。rand換算後に8を加える。 |
| [0x0065BCAC](symbols/0065BCAC.md) | global | g_UnitSearchThreshold | unit_search_bdr の現在値。初期値100で、Unit+0x1E534 にある探索カウンタと比較される。 |
| [0x0065BCFC](symbols/0065BCFC.md) | global | g_UnitStatusHpLimit | unit_status_hp の実効値。初期値100で、状態ゲージ回復の上限に使用する。 |
| [0x0065BD4C](symbols/0065BD4C.md) | global | g_UnitStatusMinValue | unit_status_min の実効値。初期値-500で、状態ゲージ減少時の下限となる。 |
| [0x0065BD58](symbols/0065BD58.md) | global | g_UnitStatusRecovery | unit_status_rec の実効値。初期値10で、自然回復時に状態ゲージへ加算される。 |
| [0x0065BD5C](symbols/0065BD5C.md) | global | g_UnitStatusDeathThreshold | unit_status_death の実効値。初期値100で、context 設定0なら unit_status_hp をコピーする。 |
| [0x0065BD9F](symbols/0065BD9F.md) | global | g_NoactiveWindowOption | 起動パラメータ noactive の処理から0にされる状態値。非アクティブ時の入力処理分岐で参照される。 |
| [0x0065BEA8](symbols/0065BEA8.md) | global | g_StatusBtnRectTable | 上の 3 つの矩形へのポインタ表（番号 0=雇用/召上げ、1=解雇、2=アイテム）。押下の当たり判定で使う |
| [0x0065BED8](symbols/0065BED8.md) | global | g_AudioBackendEntryCount | 音声プレイヤーの内部エントリー数。バックエンド生成時に4倍してポインタ配列を確保する。 |
| [0x0065BEE4](symbols/0065BEE4.md) | global | g_WindowDisplayMode | ウィンドウの表示方式の分岐値。0なら WS_POPUP/topmost のフルスクリーン風、非ゼロはウィンドウ枠付きで生成する。 |
| [0x0065BEEC](symbols/0065BEEC.md) | global | g_screenWidth | D3D バックバッファの幅として参照される設定値。高さ 0x65BEF0 とともに D3DPRESENT_PARAMETERS に渡される。 |
| [0x0065BEF0](symbols/0065BEF0.md) | global | g_ScreenHeight | 描画バックバッファの高さとして参照される値。幅 0x65BEEC と合わせて D3DPRESENT_PARAMETERS に渡す。 |
| [0x0065BF18](symbols/0065BF18.md) | global | g_DamageResistanceTable | damage_consti の11要素doubleテーブル。耐性値0〜10の基本倍率を保持し、context の非ゼロ設定が上書きする。 |
| [0x0065CD28](symbols/0065CD28.md) | global | g_SaveEmptyStringSeparator | 通常 .sav の複数グループの境界に出力される空の std::string オブジェクト。 |
| [0x0065EB64](symbols/0065EB64.md) | global | g_FourwayBattleModeFlag | 複数の戦闘経路で0と1に更新される四方向選択用状態値。用途の正式名称は未確認。 |
| [0x0067B938](symbols/0067B938.md) | global | g_BattleLimitMode | 戦闘時間制限の番兵を持つ状態。0x80000008 なら無制限扱いの戻り値に変わる。 |
| [0x0067B93C](symbols/0067B93C.md) | global | g_BattleLimitRemaining | 戦闘時間制限の現在値。無制限のときの経過カウンタにも使われる。 |
| [0x0067E978](symbols/0067E978.md) | object | g_StatusWnd | ゲーム本来のユニット詳細パネル（StatusWnd、ボタンあり） |
| [0x0067EB30](symbols/0067EB30.md) | global | g_StatusWnd_target | g_StatusWnd が表示するユニット |
| [0x0068B568](symbols/0068B568.md) | global | g_StatusBtnRect_Dismiss | 詳細パネルの「解雇」ボタンの矩形（RECT、全パネル共通） |
| [0x0068B578](symbols/0068B578.md) | global | g_StatusBtnRect_HireExtract | 詳細パネルの「雇用」「召上げ」ボタンの矩形 |
| [0x0068B588](symbols/0068B588.md) | global | g_StatusBtnRect_Item | 詳細パネルの「アイテム」ボタンの矩形。幅 0 ならアイテムボタンを出さない |
| [0x008795F0](symbols/008795F0.md) | global | g_D3DPresentParams | Reset に渡す D3DPRESENT_PARAMETERS |
| [0x00879610](symbols/00879610.md) | global | g_D3dPresentWindowedFlag | D3DPRESENT_PARAMETERS の Windowed 項目。通常は0x65BEE4に合わせて設定される。 |
| [0x00879628](symbols/00879628.md) | global | g_loadingLock | g_loadingFlag を守るクリティカルセクション |
| [0x008797FC](symbols/008797FC.md) | global | g_mainHwnd | ゲームのメインウィンドウの HWND |
| [0x0087980C](symbols/0087980C.md) | global | g_D3DDevice | IDirect3DDevice9。+0xC TestCooperativeLevel、+0x40 Reset（引数0x8795F0）、+0x44 Present、+0xAC Clear を0x4C24B0が呼ぶ |
| [0x0087981D](symbols/0087981D.md) | global | g_MusicOffStartupFlag | musicoff 起動オプションで1になる値。BGMマネージャーの生成を省略・無効化する分岐で参照される。 |
| [0x00879820](symbols/00879820.md) | global | g_TestmapStartupFlag | testmap オプションで設定される状態値。Esc からの直接終了と一部の起動モード分岐に使われる。 |
| [0x00879821](symbols/00879821.md) | global | g_ForceWindowedPresent | D3D のWindowedフラグを強制的に1にする表示上書き値。Win32側のpopup指定とは独立している。 |
| [0x00879822](symbols/00879822.md) | global | g_WindowActiveForInput | WM_ACTIVATE によって更新されるウィンドウのアクティブ値。非アクティブ時は GameMouse の buffered poll を抑制する。 |
| [0x00879823](symbols/00879823.md) | global | g_ActiveFrameGate | WndProcのWM_ACTIVATEで切り替えられるフレーム更新用のアクティブ値。入力poll側の0x879822とは別の条件を持つ。 |
| [0x0087983C](symbols/0087983C.md) | global | g_loadingFlag | 起動時ローダー実行中の印。0x555D69 で 1、0x555E15 で 0（クリティカルセクション 0x879628 の中） |
| [0x0087984F](symbols/0087984F.md) | global | g_SupportPresenceGateOverride | 支援候補の Unit+0x1D0 存在検査を切り替える条件として参照される1バイト値。具体的なゲームモードは未特定。 |
| [0x00879E48](symbols/00879E48.md) | global | g_FaceImageCache | 顔画像のキャッシュ（std::map、名前→HBITMAP）。0x4243C0が登録 |
| [0x00879E68](symbols/00879E68.md) | global | g_ChipAtlasMap | 読込み済みチップの表（std::map、要素+0x28〜+0x34が矩形）。0x424C80・0x423D70が引く |
| [0x0087A1B8](symbols/0087A1B8.md) | global | g_ChipSpriteCache | チップ画像のキャッシュ（std::map）。0x424C80が登録 |
| [0x008BA538](symbols/008BA538.md) | object | g_WarWnd | 'war' という名前の画面（WarWnd）。出撃するユニットを選ぶ間に表示される |
| [0x008BA5BC](symbols/008BA5BC.md) | global | g_WarWnd_shown | WarWnd+0x84。表示中は 0 以外。この間、詳細パネルにボタンを作らず、約 30 か所の処理が止まる |
| [0x008BA5DC](symbols/008BA5DC.md) | global | g_WarWnd_state | WarWnd+0xA4。通常時から 0x80000008 |
| [0x008BB6D8](symbols/008BB6D8.md) | object | g_ChoiceWnd | ゲーム本来の選択肢ウィンドウ（ChoiceWnd）。ラベルは index 49 まで（0x8BC11C で終わる） |
| [0x008BCD48](symbols/008BCD48.md) | object | g_TempStatusWnd | 一時表示用の詳細パネル（TempStatusWnd）。DLL のステータスパネル表示に使う |
| [0x008BCDCC](symbols/008BCDCC.md) | global | g_TempStatusWnd_visible | TempStatusWnd+0x84。表示中の印 |
| [0x008BCDE0](symbols/008BCDE0.md) | global | g_TempStatusWnd_owner | TempStatusWnd の所有者 |
| [0x008BCF00](symbols/008BCF00.md) | global | g_TempStatusWnd_target | TempStatusWnd が表示するユニット（TempStatusWnd+0x1B8）。0x55BAB0が設定し、組立て0x55BC60が顔の取得に渡す |
| [0x008BCF10](symbols/008BCF10.md) | global | g_TempStatusWnd_rects | 技能アイコンなどの矩形の配列（16 バイトずつ） |
| [0x008BE040](symbols/008BE040.md) | global | g_TempStatusWnd_hoverCount | 説明表示の対象の数 |
| [0x008BE2F0](symbols/008BE2F0.md) | object | g_GameManager | GameManager の唯一の実体（G）。スクリプトVMの文脈。DLL 側ではこのアドレスを基準 G と呼ぶ |
| [0x008BE388](symbols/008BE388.md) | global | g_NewGameMousePtr | ゲーム側で保持する NewGameMouse オブジェクトへの参照。起動時の初期化でNULLにされる。 |
| [0x008BE3A0](symbols/008BE3A0.md) | global | g_StartupVolumeMask | 起動時の音量設定計算に用いられるDWORD。musicoff状態とのAND演算で後続呼出しに渡される。 |
| [0x008BE7F4](symbols/008BE7F4.md) | global | g_Engine | スクリプトエンジン E = G+0x504 |
| [0x00AAD434](symbols/00AAD434.md) | global | g_GameManager_sceneId | 現在の場面番号（G+0x1EF144）。0=タイトル、4=シナリオ選択 など |
| [0x00AC0914](symbols/00AC0914.md) | global | g_LastPresentResult | 直前の Present の戻り値。D3DERR_DEVICELOST(0x88760868)なら0x4C24B0が復帰処理（TestCooperativeLevel→Reset）に入る |
| [0x00AC0918](symbols/00AC0918.md) | global | g_FrameStartTime | 1コマの開始時刻（timeGetTime、Sleep前）。起動直後0で、メインループ0x4C24B0だけが書く。0以外なら本ループが回っている |
| [0x00B09758](symbols/00B09758.md) | object | g_DefaultSkill | 関数内 static の既定技能。0xB0A178 bit0 が 0 なら 0x599600(__stdcall) で組み立て、atexit に 0x608900 を登録（0x57E004..0x57E02E）。即死ダメージ vf+0x70(0xF4241, …, &g_DefaultSkill, 0) の技能引数に使う |

## 構造体一覧

- [Ctx](structs/Ctx.md) — 11フィールド
- [FrameWnd](structs/FrameWnd.md) — 5フィールド
- [GameManager](structs/GameManager.md) — 9フィールド
- [GameTask](structs/GameTask.md) — 3フィールド
- [Player](structs/Player.md) — 3フィールド
- [Power](structs/Power.md) — 17フィールド
- [SaveUnitDataTreeNode](structs/SaveUnitDataTreeNode.md) — 1フィールド
- [ScriptEngine](structs/ScriptEngine.md) — 9フィールド
- [Spot](structs/Spot.md) — 10フィールド
- [StatusWnd](structs/StatusWnd.md) — 10フィールド
- [SummonRecordCacheNode](structs/SummonRecordCacheNode.md) — 1フィールド
- [TurnState](structs/TurnState.md) — 5フィールド
- [UnitDef](structs/UnitDef.md) — 34フィールド
- [UnitRuntime](structs/UnitRuntime.md) — 4フィールド

## 読み方の注意

根拠の詳細が非公開のものは、採録時の確度を維持したまま表示しています。
この事典は元の研究資料を再検証した保証書ではなく、共同調査の出発点です。
CALL情報はV9静的索引に含まれる直接CALLだけです。
