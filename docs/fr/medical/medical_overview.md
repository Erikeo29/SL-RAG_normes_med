# Synthèse du paysage normatif - dispositifs médicaux

Ce document fournit une vue d'ensemble du cadre réglementaire applicable aux
dispositifs médicaux. Il couvre les principales juridictions (États-Unis, Union
européenne, international), les normes de système de management de la qualité,
la gestion des risques, les exigences logicielles et la cybersécurité. Les
normes ISO et IEC, payantes, ne sont pas incluses dans la base RAG ; seuls les
documents publics (FDA, EU MDR/IVDR, IMDRF, MDCG, VIM) y sont indexés.

---

## Sommaire

1. [Paysage réglementaire - tableau comparatif](#1-paysage-réglementaire--tableau-comparatif)
2. [FDA - cadre réglementaire américain](#2-fda--cadre-réglementaire-américain)
3. [EU MDR 2017/745 et IVDR 2017/746](#3-eu-mdr-2017745-et-ivdr-2017746)
4. [ISO 13485 et ISO 14971 - normes internationales (non indexées)](#4-iso-13485-et-iso-14971--normes-internationales-non-indexées)
5. [Cybersécurité et logiciel médical](#5-cybersécurité-et-logiciel-médical)
6. [Articulations entre les normes - tableau croisé](#6-articulations-entre-les-normes--tableau-croisé)
7. [Documents publics indexés dans cette application](#7-documents-publics-indexés-dans-cette-application)

---

## 1. Paysage réglementaire - tableau comparatif

| Aspect | FDA (États-Unis) | EU MDR/IVDR | ISO/IEC (international) |
|---|---|---|---|
| **Autorité** | FDA - CDRH | Commission européenne, organismes notifiés | ISO, IEC (normes volontaires, souvent rendues obligatoires par référence) |
| **Classification** | Classe I, II, III (basée sur le risque) | Classe I, IIa, IIb, III (MDR) ; A, B, C, D (IVDR) | N/A - les normes s'appliquent indépendamment de la classe |
| **QMS** | 21 CFR 820 (QMSR, aligné sur ISO 13485 depuis fév. 2026) | Exigence explicite (annexe IX) du MDR | ISO 13485:2016 |
| **Gestion des risques** | Intégrée dans les design controls | Exigence essentielle (annexe I du MDR) | ISO 14971:2019 |
| **Logiciel** | Guidances FDA (SaMD, cybersécurité) | Qualification SaMD via MDCG 2019-11 | IEC 62304:2006+A1:2015 |
| **Mise sur le marché** | 510(k), PMA, De Novo | Marquage CE via organisme notifié | N/A |

---

## 2. FDA - cadre réglementaire américain

### 21 CFR 820 - quality system regulation (QMSR)

Le 21 CFR 820 définit les exigences du système qualité pour les fabricants de
dispositifs médicaux commercialisés aux États-Unis. Depuis la mise à jour QMSR
(effective 2026), le règlement s'aligne explicitement sur ISO 13485, réduisant
les divergences entre les exigences américaines et internationales. Il couvre
les design controls, la production, les CAPA, la traçabilité et la validation
des procédés.

### Guidances FDA

La FDA publie de nombreux documents d'orientation (guidances) qui précisent
l'interprétation des exigences réglementaires. Les plus pertinentes pour les
dispositifs connectés et logiciels concernent la classification SaMD (Software
as a Medical Device), la cybersécurité premarket, la soumission 510(k) et la
gestion du cycle de vie post-market. Ces guidances n'ont pas force de loi mais
représentent la position actuelle de l'agence.

### Classification et voies de mise sur le marché

Les dispositifs sont classés en trois catégories (I, II, III) selon le risque.
La classe I fait l'objet de contrôles généraux, la classe II nécessite
généralement une soumission 510(k) démontrant l'équivalence substantielle, et
la classe III requiert une approbation PMA (premarket approval) avec données
cliniques. La voie De Novo permet de classer des dispositifs nouveaux à risque
faible-modéré sans prédicat.

---

## 3. EU MDR 2017/745 et IVDR 2017/746

### MDR - règlement relatif aux dispositifs médicaux

Le règlement (UE) 2017/745 remplace les directives 93/42/CEE et 90/385/CEE.
Il renforce les exigences en matière de surveillance post-commercialisation,
d'évaluation clinique, de traçabilité (UDI) et de transparence (base EUDAMED).
La classification repose sur 22 règles (annexe VIII) et l'évaluation de
conformité passe par des organismes notifiés pour les classes supérieures à I.

### IVDR - règlement relatif aux dispositifs de diagnostic in vitro

Le règlement (UE) 2017/746 remplace la directive 98/79/CE. Il introduit une
classification en quatre classes (A, B, C, D) basée sur le risque, en
remplacement du système par listes. Les exigences de performance clinique et
de surveillance post-commercialisation sont considérablement renforcées par
rapport à l'ancienne directive.

### MDCG guidances

Les documents MDCG (Medical Device Coordination Group) fournissent des
orientations sur l'interprétation du MDR et de l'IVDR. Ils couvrent notamment
la qualification et la classification des logiciels (MDCG 2019-11), les
exigences cliniques et la surveillance post-commercialisation. Ces documents
sont publics et indexés dans la base RAG.

---

## 4. ISO 13485 et ISO 14971 - normes internationales (non indexées)

### ISO 13485:2016 - système de management de la qualité

ISO 13485 spécifie les exigences relatives au système de management de la
qualité pour les organismes impliqués dans le cycle de vie des dispositifs
médicaux. Elle est reconnue mondialement et sert de fondement aux exigences
QMS de la plupart des juridictions. Le 21 CFR 820 (QMSR) s'y aligne
désormais explicitement.

### ISO 14971:2019 - gestion des risques

ISO 14971 définit le processus de gestion des risques applicable aux
dispositifs médicaux. Elle couvre l'analyse des risques, l'évaluation, la
maîtrise et la surveillance post-production. Cette norme est référencée par
le MDR, la FDA et ISO 13485 comme cadre de gestion des risques.

**Note importante :** ces normes ISO sont protégées par le droit d'auteur et
ne sont pas disponibles en libre accès. Elles ne sont donc pas indexées dans
la base documentaire de cette application. Consultez les documents originaux
auprès de l'ISO ou de votre organisme national de normalisation.

---

## 5. Cybersécurité et logiciel médical

### Logiciel en tant que dispositif médical (SaMD)

Le concept de SaMD (Software as a Medical Device), défini par l'IMDRF,
désigne un logiciel destiné à un usage médical sans faire partie d'un
dispositif matériel. Sa classification dépend de la criticité de la décision
clinique et de la condition du patient. Les cadres FDA et EU MDR/IVDR
intègrent cette catégorisation avec des exigences adaptées.

### Cybersécurité

La FDA exige une évaluation de cybersécurité dans les soumissions premarket
(guidance 2023). Les éléments clés incluent le threat modeling, le SBOM
(Software Bill of Materials), les plans de mise à jour et de gestion des
vulnérabilités, et la conception sécurisée (security by design). Le MDR
impose des exigences similaires via l'annexe I (exigences générales de
sécurité et de performance) et les guidances MDCG.

### IEC 62304 - cycle de vie du logiciel médical

IEC 62304 définit les processus du cycle de vie du développement logiciel
pour les dispositifs médicaux. Elle introduit trois classes de sécurité
(A, B, C) déterminant le niveau de rigueur documentaire requis. Comme les
normes ISO, cette norme IEC est payante et n'est pas indexée dans la base RAG.

---

## 6. Articulations entre les normes - tableau croisé

| Thème | FDA | EU MDR/IVDR | ISO/IEC |
|---|---|---|---|
| Système qualité | 21 CFR 820 (QMSR) | Annexes IX, XI | ISO 13485 |
| Gestion des risques | QMSR (via ISO 13485 cl. 7.1, 7.3) | Annexe I, exigences générales | ISO 14971 |
| Logiciel | Guidances SaMD, cybersécurité | MDCG 2019-11, annexe I | IEC 62304 |
| Évaluation clinique | Clinical trials, 510(k) | Annexes XIV, XV | ISO 14155 |
| Surveillance post-market | 21 CFR 803/822 (MDR reporting) | Chapitre VII (MDR) | ISO 13485 §8.2.1 |
| Traçabilité (UDI) | 21 CFR 830 | Article 27 (MDR) | IMDRF UDI guidance |
| Biocompatibilité | Guidance FDA | Annexe I | ISO 10993 |

Les trois piliers (FDA, EU MDR, ISO/IEC) se chevauchent largement. L'alignement
du 21 CFR 820 sur ISO 13485 (QMSR 2026) simplifie la conformité simultanée.
ISO 14971 est le référentiel commun de gestion des risques reconnu par toutes
les juridictions.

---

## 7. Documents publics indexés dans cette application

La base documentaire RAG contient uniquement des documents en libre accès :

- **FDA** : guidances (cybersécurité, inspections quality systems, MDQS manual, quality system regulation overview).
- **EU MDR/IVDR** : textes des règlements 2017/745 et 2017/746.
- **MDCG** : MDCG 2020-6 (evidence clinique suffisante).
- **IMDRF** : N47 (principes essentiels de sécurité et de performance).
- **VIM** : vocabulaire international de métrologie.

Les normes ISO (13485, 14971, 10993) et IEC (62304) ne sont **pas** incluses
car elles sont protégées par le droit d'auteur et disponibles uniquement sous
licence payante. Pour ces normes, référez-vous aux documents originaux.
