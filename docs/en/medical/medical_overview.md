# Overview of the regulatory landscape - medical devices

This document provides an overview of the regulatory framework applicable to
medical devices. It covers the main jurisdictions (United States, European
Union, international), quality management system standards, risk management,
software requirements, and cybersecurity. ISO and IEC standards, which are
copyrighted and require purchase, are not included in the RAG database; only
publicly available documents (FDA, EU MDR/IVDR, IMDRF, MDCG, VIM) are indexed.

---

## Table of contents

1. [Regulatory landscape - comparative table](#1-regulatory-landscape--comparative-table)
2. [FDA - US regulatory framework](#2-fda--us-regulatory-framework)
3. [EU MDR 2017/745 and IVDR 2017/746](#3-eu-mdr-2017745-and-ivdr-2017746)
4. [ISO 13485 and ISO 14971 - international standards (not indexed)](#4-iso-13485-and-iso-14971--international-standards-not-indexed)
5. [Cybersecurity and medical software](#5-cybersecurity-and-medical-software)
6. [Interconnections between standards - cross-reference table](#6-interconnections-between-standards--cross-reference-table)
7. [Public documents indexed in this application](#7-public-documents-indexed-in-this-application)

---

## 1. Regulatory landscape - comparative table

| Aspect | FDA (United States) | EU MDR/IVDR | ISO/IEC (international) |
|---|---|---|---|
| **Authority** | FDA - CDRH | European Commission, notified bodies | ISO, IEC (voluntary standards, often made mandatory by reference) |
| **Classification** | Class I, II, III (risk-based) | Class I, IIa, IIb, III (MDR); A, B, C, D (IVDR) | N/A - standards apply regardless of class |
| **QMS** | 21 CFR 820 (QMSR, aligned with ISO 13485 since Feb. 2026) | Explicit requirement (Annex IX) of MDR | ISO 13485:2016 |
| **Risk management** | Integrated in design controls | Essential requirement (MDR Annex I) | ISO 14971:2019 |
| **Software** | FDA guidances (SaMD, cybersecurity) | SaMD qualification via MDCG 2019-11 | IEC 62304:2006+A1:2015 |
| **Market access** | 510(k), PMA, De Novo | CE marking via notified body | N/A |

---

## 2. FDA - US regulatory framework

### 21 CFR 820 - quality system regulation (QMSR)

21 CFR 820 defines quality system requirements for manufacturers of medical
devices marketed in the United States. Since the QMSR update (effective 2026),
the regulation explicitly aligns with ISO 13485, reducing the divergence
between US and international requirements. It covers design controls,
production, CAPA, traceability, and process validation.

### FDA guidances

The FDA publishes numerous guidance documents that clarify the interpretation
of regulatory requirements. The most relevant ones for connected devices and
software address SaMD (Software as a Medical Device) classification, premarket
cybersecurity, 510(k) submissions, and post-market life cycle management.
Guidances do not have the force of law but represent the agency's current
position.

### Classification and market authorization pathways

Devices are classified into three categories (I, II, III) based on risk.
Class I devices are subject to general controls, Class II generally requires
a 510(k) submission demonstrating substantial equivalence, and Class III
requires PMA (premarket approval) with clinical data. The De Novo pathway
allows classification of novel low-to-moderate risk devices without a
predicate.

---

## 3. EU MDR 2017/745 and IVDR 2017/746

### MDR - medical devices regulation

Regulation (EU) 2017/745 replaces Directives 93/42/EEC and 90/385/EEC. It
strengthens requirements for post-market surveillance, clinical evaluation,
traceability (UDI), and transparency (EUDAMED database). Classification is
based on 22 rules (Annex VIII), and conformity assessment involves notified
bodies for classes above I.

### IVDR - in vitro diagnostic devices regulation

Regulation (EU) 2017/746 replaces Directive 98/79/EC. It introduces a
four-class system (A, B, C, D) based on risk, replacing the previous
list-based approach. Clinical performance and post-market surveillance
requirements are considerably strengthened compared to the former directive.

### MDCG guidances

MDCG (Medical Device Coordination Group) documents provide guidance on the
interpretation of the MDR and IVDR. They cover software qualification and
classification (MDCG 2019-11), clinical requirements, and post-market
surveillance, among other topics. These documents are publicly available and
indexed in the RAG database.

---

## 4. ISO 13485 and ISO 14971 - international standards (not indexed)

### ISO 13485:2016 - quality management system

ISO 13485 specifies quality management system requirements for organizations
involved in the life cycle of medical devices. It is recognized worldwide and
serves as the foundation for QMS requirements in most jurisdictions. The
21 CFR 820 (QMSR) now explicitly aligns with it.

### ISO 14971:2019 - risk management

ISO 14971 defines the risk management process applicable to medical devices.
It covers risk analysis, evaluation, control, and post-production monitoring.
This standard is referenced by the MDR, the FDA, and ISO 13485 as the risk
management framework.

**Important note:** these ISO standards are protected by copyright and are not
freely available. They are therefore not indexed in this application's document
database. Consult the original documents through ISO or your national
standards body.

---

## 5. Cybersecurity and medical software

### Software as a medical device (SaMD)

The SaMD (Software as a Medical Device) concept, defined by the IMDRF,
designates software intended for medical use without being part of a hardware
device. Its classification depends on the criticality of the clinical decision
and the patient's condition. Both FDA and EU MDR/IVDR frameworks incorporate
this categorization with adapted requirements.

### Cybersecurity

The FDA requires a cybersecurity assessment in premarket submissions (2023
guidance). Key elements include threat modeling, SBOM (Software Bill of
Materials), update and vulnerability management plans, and security by design.
The MDR imposes similar requirements through Annex I (general safety and
performance requirements) and MDCG guidances.

### IEC 62304 - medical software life cycle

IEC 62304 defines the life cycle processes for medical device software
development. It introduces three safety classes (A, B, C) that determine the
level of documentation rigor required. Like ISO standards, this IEC standard
requires purchase and is not indexed in the RAG database.

---

## 6. Interconnections between standards - cross-reference table

| Topic | FDA | EU MDR/IVDR | ISO/IEC |
|---|---|---|---|
| Quality system | 21 CFR 820 (QMSR) | Annexes IX, XI | ISO 13485 |
| Risk management | QMSR (via ISO 13485 cl. 7.1, 7.3) | Annex I, general requirements | ISO 14971 |
| Software | SaMD and cybersecurity guidances | MDCG 2019-11, Annex I | IEC 62304 |
| Clinical evaluation | Clinical trials, 510(k) | Annexes XIV, XV | ISO 14155 |
| Post-market surveillance | 21 CFR 803/822 (MDR reporting) | Chapter VII (MDR) | ISO 13485 §8.2.1 |
| Traceability (UDI) | 21 CFR 830 | Article 27 (MDR) | IMDRF UDI guidance |
| Biocompatibility | FDA guidance | Annex I | ISO 10993 |

The three pillars (FDA, EU MDR, ISO/IEC) overlap significantly. The alignment
of 21 CFR 820 with ISO 13485 (QMSR 2026) simplifies simultaneous compliance.
ISO 14971 is the common risk management framework recognized across all
jurisdictions.

---

## 7. Public documents indexed in this application

The RAG document database contains only freely accessible documents:

- **FDA**: guidances (cybersecurity, inspections quality systems, MDQS manual, quality system regulation overview).
- **EU MDR/IVDR**: full text of Regulations 2017/745 and 2017/746.
- **MDCG**: MDCG 2020-6 (sufficient clinical evidence).
- **IMDRF**: N47 (essential principles of safety and performance).
- **VIM**: international vocabulary of metrology.

ISO standards (13485, 14971, 10993) and IEC standards (62304) are **not**
included because they are protected by copyright and available only under
paid license. For these standards, refer to the original documents.
