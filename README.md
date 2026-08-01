# daizu-s-block-list

daizu-007が管理する[uBlock Origin](https://github.com/gorhill/uBlock)のブロックリストです。

基本的にEasy ListとuBlock Filtersを使用するため広告ブロック用フィルターは作成しないと思います。  
また、偽サイトについても[uB-filter-by-kdroidwin](https://github.com/Kdroidwin/uB-filter-by-kdroidwin)を使用しているため対応しません。

個人用なので有用性は低いと思います。

## フィルターリスト

### Twitter

#### daizu's twitter mute words

Twitterで不快なポストを非表示にするためのフィルターです。アカウントに関わらず、また抜け漏れなく、検索結果も含めてブロックします。  
このフィルターは、Twitterの投稿から受けるストレスの軽減を目指しているもので、言葉狩りや表現規制に賛同するものではなく、むしろ自衛を容易にすることで表現の自由の保護につながると考えています。

[インストール](https://subscribe.adblockplus.org/?location=https%3A%2F%2Fraw.githubusercontent.com%2Fdaizu-007%2Fdaizu-s-block-list%2Frefs%2Fheads%2Fmain%2FTwitter%2Fmute_words.txt\&title=daizu%27s%20twitter%20mute%20words)

```
https://raw.githubusercontent.com/daizu-007/daizu-s-block-list/refs/heads/main/Twitter/mute_words.txt
```

#### I don't need old news on Twitter

Twitterで古いニュースを非表示にします。現在は、Gigazineの過去記事再投稿(投稿の最後に投稿年が書かれた投稿)のみが対象です。

[インストール](https://subscribe.adblockplus.org/?location=https%3A%2F%2Fraw.githubusercontent.com%2Fdaizu-007%2Fdaizu-s-block-list%2Frefs%2Fheads%2Fmain%2FTwitter%2Fold_news.txt\&title=I%20don%27t%20need%20old%20news%20on%20Twitter)

```
https://raw.githubusercontent.com/daizu-007/daizu-s-block-list/refs/heads/main/Twitter/old_news.txt
```

#### daizu's twitter mute users

一部のTwitterユーザーの投稿を非表示にします。独断と偏見でストレスの原因になりやすそうなユーザーを選びました。  
対象ユーザーの主張に賛同/反対するものではなく、また当人を攻撃する意思もありません。当人に全く非がない場合でも、周囲の反応等でストレスになる可能性があると判断した場合はブロック対象にしています。  
issueやDM等で連絡をくださればブロック対象から外す等の対応も可能です。

[インストール](https://subscribe.adblockplus.org/?location=https%3A%2F%2Fraw.githubusercontent.com%2Fdaizu-007%2Fdaizu-s-block-list%2Frefs%2Fheads%2Fmain%2FTwitter%2Fmute_users.txt\&title=daizu%27s%20twitter%20mute%20users)

```
https://raw.githubusercontent.com/daizu-007/daizu-s-block-list/refs/heads/main/Twitter/mute_users.txt
```

### YouTube

#### YouTube End Screen

YouTube動画の最後に表示されるオーバーレイコンテンツを可能な限り非表示にするためのフィルターです。

[インストール](https://subscribe.adblockplus.org/?location=https%3A%2F%2Fraw.githubusercontent.com%2Fdaizu-007%2Fdaizu-s-block-list%2Frefs%2Fheads%2Fmain%2FYouTube%2Fend_screen.txt\&title=Hide%20YouTube%20End%20Screen%20Contents)

```
https://raw.githubusercontent.com/daizu-007/daizu-s-block-list/refs/heads/main/YouTube/end_screen.txt
```

## クレジット
このフィルターリストの作成にあたって、以下を参考にさせていただきました。
- [uB-filter-by-kdroidwin](https://github.com/Kdroidwin/uB-filter-by-kdroidwin) by [Kdroidwin](https://github.com/Kdroidwin): uBlockOrigin向けリストの基本形を参考にしました
- [gist:488dac5770c2a3cc36edc9139b625190](https://gist.github.com/Yuki2718/488dac5770c2a3cc36edc9139b625190) by [Yuki2718](https://github.com/Yuki2718): Twitterで特定ユーザーの投稿を非表示にする方法を参考にしました  
  
このフィルターの作成に協力してくださったすべての方に感謝を申し上げます。以下に、主な貢献者の主な貢献内容を記載します。
- [Kdroidwin](https://github.com/Kdroidwin)
  - [直接インストールできるリンクの追加](https://github.com/daizu-007/daizu-s-block-list/pull/1)
  - [Twitter向けミュートワードの追加](https://github.com/daizu-007/daizu-s-block-list/pull/1)
- [Yuki2718](https://github.com/Yuki2718)
  - [uBlock Originで特定ユーザーの投稿を非表示にする方法の提供](https://x.com/Yuki27183/status/2082784790269534284?s=20)