# Prompts Seedance 2.5 : regarder, copier, créer

[English](README_EN.md) · [简体中文](README_ZH.md) · [繁體中文](README_TW.md) · [日本語](README_JA.md) · [Português](README_PT.md) · [Español](README_ES.md) · [Deutsch](README_DE.md) · [Русский](README_RU.md) · [Français](README_FR.md) · [한국어](README_KO.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md) · [Bahasa Indonesia](README_ID.md) · [Italiano](README_IT.md)

![Un tramway orange suit des rails courbes dans une rue qui passe du croquis aux maquettes en papier, puis aux bâtiments réalistes éclairés de lumière chaude. Couverture créée avec l’IA, pas une vidéo Seedance.](assets/seaimagine-seedance-hero-v5.jpg)

Une scène originale évoque la création, de l’esquisse des structures aux matières, à la lumière et au mouvement.

Cette édition SeaImagine reprend le dépôt Flaq de notre entreprise : 120 recettes, dont 60 en chinois et 60 en anglais. Les compléments en 14 langues proposent six exercices chacun ; les 120 recettes ne sont pas toutes traduites dans chaque langue.

## Commencer par un seul plan

Choisissez une scène dans l’index, copiez le prompt, puis adaptez le sujet, les matières et le mouvement de caméra. Utilisez une image dont vous détenez les droits nécessaires. Dans SeaImagine, choisissez un mode d’entrée et une durée disponibles ; vérifiez le résultat avant de le prolonger.

[Index des 120 recettes](prompts/README.md) · [Six exercices en français](prompts/i18n/prompt-library.fr.md)

## Créer avec SeaImagine

Ouvrez la page Seedance pour accéder au modèle. Create permet de préparer des références visuelles et de trouver les outils d’image et de vidéo. Consultez les disponibilités, tarifs et limites dans l’interface. Les durées suggérées sont des intentions créatives, pas des garanties du service.

[SeaImagine · Seedance 2.5](https://seaimagine.com/fr/model/seedance-2-5/) · [SeaImagine · Create](https://seaimagine.com/fr/create/)

## Apprendre des vidéos de la communauté

Le modèle est celui déclaré par l’auteur. Ces vidéos sont des œuvres de créateurs externes ; nous n’avons pas vérifié si elles ont été générées avec SeaImagine. Cliquez sur la miniature pour voir la vidéo et consultez le prompt dans la publication originale. Il s’agit de références éditoriales, pas d’un classement de popularité vérifié.

### Cuisine et synchronisation sonore

[![Cuisine et synchronisation sonore — @Goodmanprotocol](https://pbs.twimg.com/amplify_video_thumb/2099186062715404288/img/D-iYamhA_iFRBooM.jpg)](https://video.twimg.com/amplify_video/2099186062715404288/vid/avc1/1920x1080/H8uxwKxVsSU09_LW.mp4?tag=29)

[Publication originale et prompt de l’auteur](https://x.com/Goodmanprotocol/status/2099186117769822462) · **@Goodmanprotocol**

Observez comment les gros plans et les sons synchronisés préparent la chute comique.

### Un vêtement, plusieurs tenues

[![Un vêtement, plusieurs tenues — @Goodmanprotocol](https://pbs.twimg.com/amplify_video_thumb/2095216899445649408/img/690ykZJzst5uQLwH.jpg)](https://video.twimg.com/amplify_video/2095216899445649408/vid/avc1/1920x1080/LZt4YKiTkMag5Db1.mp4?tag=29)

[Publication originale et prompt de l’auteur](https://x.com/Goodmanprotocol/status/2095216981624721691) · **@Goodmanprotocol**

Conservez la couleur et la coupe du vêtement ; reliez les tenues par des mouvements similaires.

[Les 12 exemples de la communauté](README.md) · [Exemples officiels et sources](docs/official-examples.md)

## Structure du prompt

```text
[Objectif] audience, usage, durée, format
[Références] rôle unique de chaque image ou vidéo
[Invariants] identité, produit, décor et éclairage à préserver
[Chronologie] mise en place → action → révélation → plan final
[Caméra] cadrage, hauteur, trajectoire, vitesse, mise au point, arrêt
[Son] dialogue, ambiance, bruitage, musique et synchronisation
[À éviter] dérive, doublons, anatomie, faux texte, logos, watermark
```

## Copier un prompt complet de produit

![Image de référence de thé pétillant](assets/product-sparkling-tea-reference.png)

Image de référence provenant du dépôt source Flaq, pas un résultat vidéo. Vous pouvez l’utiliser directement comme image d’entrée pour cet exercice.

Préparez une image de référence d’une bouteille sans marque. Cet exercice n’est pas le prompt des vidéos ci-dessus ; aucun test de génération n’est revendiqué. Raccourcissez ou découpez la séquence selon les limites de l’interface.

```text
Utiliser la bouteille en verre de l'Image 1 comme unique référence produit. Conserver sa silhouette, son bouchon, les proportions de l'étiquette vierge, le niveau du liquide ambré, la condensation et la direction de la lumière. Ne générer aucun texte.

00:00–00:05 : macro sur une goutte puis transfert de mise au point vers les bulles fines. 00:05–00:11 : rotation horaire de 35 degrés avec lent recul ; la glace réfracte naturellement et la bouteille reste stable. 00:11–00:17 : un contre-jour chaud passe derrière ; le bouchon se soulève à peine et libère une brume discrète. 00:17–00:24 : descendre vers un angle héroïque et s'arrêter sur une vue frontale avec espace libre en haut.

Son : bouchon, fines bulles, glace et rythme original minimal. Pas de bouteille ajoutée, dérive d'étiquette, verre déformé, liquide traversant, faux texte, logo, marque ou filigrane.
```

[Six exercices en français](prompts/i18n/prompt-library.fr.md) · [Index des 120 recettes](prompts/README.md) · [Guide de création](docs/seaimagine-workflow.md) · [Sources et attribution](docs/PROVENANCE.md)

[Flaq · GitHub](https://github.com/flaqai/awesome_seedance_2_5) · [SeaImagine · GitHub](https://github.com/seaimagineai/awesome-seedance-2-5-prompts)
