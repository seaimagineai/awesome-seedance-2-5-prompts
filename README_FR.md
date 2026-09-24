# Prompts Seedance 2.5 : regarder, copier, créer

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_TW.md) · [日本語](README_JA.md) · [Português](README_PT.md) · [Español](README_ES.md) · [Deutsch](README_DE.md) · [Русский](README_RU.md) · [Français](README_FR.md) · [한국어](README_KO.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md) · [Bahasa Indonesia](README_ID.md) · [Italiano](README_IT.md)

![Un tramway orange suit des rails courbes dans une rue qui passe du croquis aux maquettes en papier, puis aux bâtiments réalistes éclairés de lumière chaude.](assets/seaimagine-seedance-hero-v5.jpg)

Une scène originale évoque la création, de l’esquisse des structures aux matières, à la lumière et au mouvement.

La collection comprend 120 recettes : 60 en chinois et 60 en anglais. Commencez par les six exercices en français et adaptez-les à vos idées.

## Commencer par un seul plan

Choisissez un des exercices en français ci-dessous, puis adaptez le sujet, les matières et le mouvement de caméra. Dans SeaImagine, sélectionnez le mode et la durée, puis examinez une courte séquence avant de poursuivre.

[Six exercices en français](prompts/i18n/prompt-library.fr.md) · [Index des 120 recettes · en chinois simplifié](prompts/README.md)

## Apprendre des vidéos de la communauté

Ouvrez les miniatures pour observer le mouvement et le son. Chaque exemple renvoie aussi à la publication de son auteur.

### Cuisine et synchronisation sonore

[![Cuisine et synchronisation sonore — @Goodmanprotocol](https://pbs.twimg.com/amplify_video_thumb/2099186062715404288/img/D-iYamhA_iFRBooM.jpg)](https://video.twimg.com/amplify_video/2099186062715404288/vid/avc1/1920x1080/H8uxwKxVsSU09_LW.mp4?tag=29)

[Publication originale et prompt de l’auteur](https://x.com/Goodmanprotocol/status/2099186117769822462) · **@Goodmanprotocol**

Observez comment les gros plans et les sons synchronisés préparent la chute comique.

### Un vêtement, plusieurs tenues

[![Un vêtement, plusieurs tenues — @Goodmanprotocol](https://pbs.twimg.com/amplify_video_thumb/2095216899445649408/img/690ykZJzst5uQLwH.jpg)](https://video.twimg.com/amplify_video/2095216899445649408/vid/avc1/1920x1080/LZt4YKiTkMag5Db1.mp4?tag=29)

[Publication originale et prompt de l’auteur](https://x.com/Goodmanprotocol/status/2095216981624721691) · **@Goodmanprotocol**

Conservez la couleur et la coupe du vêtement ; reliez les tenues par des mouvements similaires.

[Les 12 exemples de la communauté · en anglais](README.md) · [Exemples officiels et sources · en anglais](docs/official-examples.md)

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

Préparez une image de bouteille sans marque en vous inspirant de l’image ci-dessus. Commencez par cinq secondes de gouttes et de bulles ; pour la séquence complète, adaptez la durée aux options de l’interface.

```text
Utiliser la bouteille en verre de l'Image 1 comme unique référence produit. Conserver sa silhouette, son bouchon, les proportions de l'étiquette vierge, le niveau du liquide ambré, la condensation et la direction de la lumière. Ne générer aucun texte.

00:00–00:05 : macro sur une goutte puis transfert de mise au point vers les bulles fines. 00:05–00:11 : rotation horaire de 35 degrés avec lent recul ; la glace réfracte naturellement et la bouteille reste stable. 00:11–00:17 : un contre-jour chaud passe derrière ; le bouchon se soulève à peine et libère une brume discrète. 00:17–00:24 : descendre vers un angle héroïque et s'arrêter sur une vue frontale avec espace libre en haut.

Son : bouchon, fines bulles, glace et rythme original minimal. Pas de bouteille ajoutée, dérive d'étiquette, verre déformé, liquide traversant, faux texte, logo, marque ou filigrane.
```

## Créer avec SeaImagine

![Un voilier doré sur une mer de papier, éclairé par un phare.](assets/seaimagine-paper-sea.jpg)

Reprenez les principes du produit — préserver la forme, décrire la matière et guider la caméra — pour raconter une petite histoire. Dans SeaImagine, partez d’un texte et essayez cette proposition de 5 secondes.

```text
5 secondes, un seul plan. Un voilier en papier doré avance lentement sur des vagues de papier bleu canard. La caméra le suit à hauteur basse ; un phare lointain diffuse une lumière chaude. Conserver la coque, la voile et les fibres du papier. Finir en douceur. Sans texte, logo, bateau supplémentaire ni déformation.
```

[SeaImagine · Seedance 2.5](https://seaimagine.com/fr/model/seedance-2-5/) · [SeaImagine · Create](https://seaimagine.com/fr/create/)

[Six exercices en français](prompts/i18n/prompt-library.fr.md) · [Index des 120 recettes · en chinois simplifié](prompts/README.md) · [Guide de création · en anglais](docs/seaimagine-workflow.md)

[SeaImagine · GitHub](https://github.com/seaimagineai/awesome-seedance-2-5-prompts)

## Sources et utilisation des images

La couverture, la mer de papier et la référence produit sont des images fixes créées par IA, et non des résultats vidéo. Les exercices sont des adaptations éditoriales, pas les instructions originales des vidéos présentées, et n’ont pas été testés par génération. Les modèles des vidéos externes sont indiqués d’après leurs auteurs. Consultez les droits et conditions dans les [sources (en anglais)](docs/PROVENANCE.md) et la [licence (en anglais)](LICENSE).
