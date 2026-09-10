/* Wymagania edukacyjne z informatyki – klasa 1W, branżowa szkoła I stopnia.
 *
 * Źródła treści:
 *   rozklad_1W.docx      – rozkład materiału nauczania (30 tematów, 30 godzin)
 *   plan_wynikowy.docx   – plan wynikowy z wymaganiami na pięć poziomów ocen
 * Oba dokumenty scala budujdane.py do daneSB.js.
 *
 * Blok „ocenianie" pochodzi ze wspólnego wzo.js – tego samego, którego używają
 * dokumenty dla 1TT, 2LOA, 3TT, 4TI i ASSO. Dzięki temu zapisy statutu brzmią
 * we wszystkich przedmiotach identycznie.
 */
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
  LevelFormat, PageBreak, Footer, PageNumber
} = require("docx");
const fs = require("fs");
const WZO = require("./wzo.js");
const { dzialy } = require("./daneSB.js");

const W = 9638;                 // szerokość kolumny tekstu (A4, marginesy 2 cm)
const GRAY = "F2F2F2";
const HEAD = "D9E2F3";
const ACCENT = "1F4E79";

const P = (text, opts = {}) => new Paragraph({
  alignment: opts.align,
  spacing: { before: opts.before ?? 0, after: opts.after ?? 100, line: 264 },
  indent: opts.indent,
  children: [new TextRun({
    text, bold: opts.bold, italics: opts.italics,
    size: opts.size ?? 21, color: opts.color, font: "Calibri"
  })]
});

const bullet = (text, size = 20) => new Paragraph({
  numbering: { reference: "punkty", level: 0 },
  spacing: { after: 40, line: 252 },
  children: [new TextRun({ text, size, font: "Calibri" })]
});

const cell = (children, width, opts = {}) => new TableCell({
  width: { size: width, type: WidthType.DXA },
  shading: opts.fill ? { type: ShadingType.CLEAR, fill: opts.fill, color: "auto" } : undefined,
  verticalAlign: opts.valign ?? "top",
  margins: { top: 60, bottom: 60, left: 100, right: 100 },
  children
});

const hcell = (text, width) => cell(
  [new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 0 },
    children: [new TextRun({ text, bold: true, size: 20, font: "Calibri", color: "1F3864" })]
  })], width, { fill: HEAD, valign: "center" });

// ---------- tabela tematów działu ----------
function tabelaTematow(d) {
  // Nagłówek ostatniej kolumny to jedno długie słowo („podręcznika"), więc
  // kolumna musi być na tyle szeroka, żeby Word nie łamał go w środku.
  const cols = [700, 5938, 1300, 1700];
  const rows = [new TableRow({
    tableHeader: true,
    children: [hcell("Lp.", cols[0]), hcell("Temat zajęć", cols[1]),
               hcell("Liczba godzin", cols[2]), hcell("Rozdział podręcznika", cols[3])]
  })];
  d.tematy.forEach((t, i) => {
    const fill = i % 2 ? GRAY : undefined;
    rows.push(new TableRow({
      children: [
        cell([new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 }, children: [new TextRun({ text: String(t.lp), size: 19, font: "Calibri" })] })], cols[0], { fill, valign: "center" }),
        cell([new Paragraph({ spacing: { after: 0 }, children: [new TextRun({ text: t.tytul, size: 19, font: "Calibri" })] })], cols[1], { fill }),
        cell([new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 }, children: [new TextRun({ text: String(t.godziny), size: 19, font: "Calibri" })] })], cols[2], { fill, valign: "center" }),
        cell([new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 }, children: [new TextRun({ text: t.rozdzial, size: 19, font: "Calibri", color: "595959" })] })], cols[3], { fill, valign: "center" })
      ]
    }));
  });
  rows.push(new TableRow({
    children: [
      cell([new Paragraph({ spacing: { after: 0 }, children: [] })], cols[0], { fill: HEAD }),
      cell([new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { after: 0 }, children: [new TextRun({ text: "Razem:", bold: true, size: 19, font: "Calibri" })] })], cols[1], { fill: HEAD }),
      cell([new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 }, children: [new TextRun({ text: String(d.godziny), bold: true, size: 19, font: "Calibri" })] })], cols[2], { fill: HEAD, valign: "center" }),
      cell([new Paragraph({ spacing: { after: 0 }, children: [] })], cols[3], { fill: HEAD })
    ]
  }));
  return new Table({ columnWidths: cols, width: { size: W, type: WidthType.DXA }, rows });
}

// ---------- tabela wymagań na oceny ----------
const POZIOMY = [
  ["dop", "dopuszczająca (2)", "wymagania konieczne"],
  ["dst", "dostateczna (3)", "wymagania podstawowe"],
  ["db", "dobra (4)", "wymagania rozszerzające"],
  ["bdb", "bardzo dobra (5)", "wymagania dopełniające"],
  ["cel", "celująca (6)", "wymagania wykraczające"]
];

function tabelaWymagan(d) {
  const cols = [1900, 7738];
  const rows = [new TableRow({
    tableHeader: true,
    children: [hcell("Ocena", cols[0]), hcell("Uczeń:", cols[1])]
  })];
  POZIOMY.forEach(([klucz, nazwa, opis], i) => {
    const fill = i % 2 ? GRAY : undefined;
    const lewa = [
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: [new TextRun({ text: nazwa, bold: true, size: 20, font: "Calibri", color: ACCENT })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 }, children: [new TextRun({ text: opis, italics: true, size: 17, font: "Calibri", color: "595959" })] })
    ];
    const prawa = [];
    if (klucz !== "dop") {
      prawa.push(new Paragraph({
        spacing: { after: 60 },
        children: [new TextRun({ text: "spełnia wymagania na ocenę niższą, a ponadto:", italics: true, size: 18, font: "Calibri", color: "595959" })]
      }));
    }
    d.oceny[klucz].forEach(t => prawa.push(bullet(t)));
    rows.push(new TableRow({
      cantSplit: d.oceny[klucz].length <= 6,
      children: [cell(lewa, cols[0], { fill, valign: "center" }), cell(prawa, cols[1], { fill })]
    }));
  });
  return new Table({ columnWidths: cols, width: { size: W, type: WidthType.DXA }, rows });
}

// ---------- treść dokumentu ----------
const body = [];
const RAZEM = dzialy.reduce((s, d) => s + d.godziny, 0);

body.push(new Paragraph({
  alignment: AlignmentType.CENTER, spacing: { after: 60 },
  children: [new TextRun({ text: "Powiatowe Centrum Edukacji i Kształcenia Zawodowego w Szczucinie", size: 20, font: "Calibri", color: "595959" })]
}));
body.push(new Paragraph({
  alignment: AlignmentType.CENTER, spacing: { before: 240, after: 80 },
  children: [new TextRun({ text: "WYMAGANIA EDUKACYJNE Z INFORMATYKI", bold: true, size: 32, font: "Calibri", color: ACCENT })]
}));
body.push(new Paragraph({
  alignment: AlignmentType.CENTER, spacing: { after: 40 },
  children: [new TextRun({ text: "branżowa szkoła I stopnia · klasa 1W · 1 godzina tygodniowo", size: 22, font: "Calibri" })]
}));
body.push(new Paragraph({
  alignment: AlignmentType.CENTER, spacing: { after: 320 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: ACCENT, space: 6 } },
  children: [new TextRun({ text: `łącznie ${RAZEM} godzin w roku szkolnym`, size: 20, font: "Calibri", color: "595959" })]
}));

body.push(new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 200, after: 120 }, children: [new TextRun({ text: "1. Postanowienia ogólne", bold: true, size: 26, font: "Calibri", color: ACCENT })] }));

[
  "Wymagania edukacyjne opracowano na podstawie rozkładu materiału nauczania informatyki dla branżowej szkoły I stopnia (klasa 1) oraz planu wynikowego z wymaganiami edukacyjnymi do tego rozkładu.",
  "Wymagania są zgodne z podstawą programową kształcenia ogólnego z informatyki dla branżowej szkoły I stopnia. Układ działów odpowiada pięciu obszarom podstawy programowej: rozumieniu i rozwiązywaniu problemów, programowaniu, posługiwaniu się komputerem i sieciami, rozwijaniu kompetencji społecznych oraz przestrzeganiu prawa i zasad bezpieczeństwa.",
  "Informatyka w branżowej szkole I stopnia jest realizowana w wymiarze jednej godziny tygodniowo w klasie pierwszej, co daje 30 godzin w cyklu kształcenia. Każdemu tematowi odpowiada jedna jednostka lekcyjna.",
  "Na pierwszej lekcji, w ramach tematu 1, uczniowie zapoznają się z niniejszymi wymaganiami edukacyjnymi oraz z regulaminem i zasadami bhp obowiązującymi w pracowni komputerowej.",
  "Wymagania na poszczególne oceny mają charakter kumulatywny: aby otrzymać daną ocenę, uczeń musi spełniać także wymagania na wszystkie oceny niższe. Wymagania na ocenę dopuszczającą i dostateczną odpowiadają wymaganiom podstawowym planu wynikowego, wymagania na ocenę dobrą, bardzo dobrą i celującą – wymaganiom ponadpodstawowym.",
  "Ocenę niedostateczną (1) otrzymuje uczeń, który nie spełnia wymagań na ocenę dopuszczającą, tj. nie opanował podstawowych wiadomości i umiejętności umożliwiających kontynuowanie nauki przedmiotu i nie wykonuje zadań o elementarnym stopniu trudności nawet z pomocą nauczyciela.",
  "Przy jednej godzinie tygodniowo podstawą oceny jest praca na lekcji. Uczeń, który systematycznie wykonuje ćwiczenia przy komputerze i oddaje je w wyznaczonym terminie, gromadzi oceny bieżące bez konieczności pisania dodatkowych prac."
].forEach(t => body.push(P(t, { after: 120 })));

body.push(P("Formy sprawdzania osiągnięć ucznia:", { bold: true, before: 120, after: 60 }));
[
  "ćwiczenia i zadania praktyczne wykonywane przy komputerze – podstawowa forma oceniania na tym przedmiocie;",
  "prace kontrolne podsumowujące dział, zapowiadane z co najmniej tygodniowym wyprzedzeniem;",
  "kartkówki z bieżącego materiału (do trzech ostatnich lekcji), niewymagające zapowiedzi;",
  "projekty – dokument, arkusz, model 3D, materiał reklamowy lub prezentacja – oceniane za efekt końcowy, samodzielność i zgodność z poleceniem;",
  "odpowiedzi ustne, aktywność na lekcji oraz praca domowa;",
  "osiągnięcia w konkursach informatycznych i zawodowych."
].forEach(t => body.push(bullet(t, 21)));

WZO.sekcje({
  formaM: "praca kontrolna podsumowująca dział",
  formaD: "pracy kontrolnej podsumowującej dział",
  formaZ: "ją",
  olimpiada: "olimpiady informatycznej",
  praktyczne: true,
  extraZaleglosci: [
    "przy jednej godzinie tygodniowo ćwiczenie niedokończone na lekcji uczeń oddaje do końca następnego tygodnia – w tym czasie ocena pozostaje niewystawiona;"
  ]
}).forEach(g => {
  body.push(P(g.tytul, { bold: true, before: 140, after: 50, size: 21 }));
  if (g.wstep) body.push(P(g.wstep, { italics: true, size: 20, color: "595959", after: 60 }));
  g.punkty.forEach(t => body.push(bullet(t, 21)));
});
body.push(P(WZO.stopka, { italics: true, size: 20, color: "595959", before: 140, after: 60 }));

body.push(P("Materiały do przedmiotu – spis tematów, wymagania i zadania – są dostępne na stronie: https://josimate.github.io/inf-sb/", { italics: true, before: 160, after: 200, size: 20, color: "595959" }));

// ---- rozkład godzin ----
body.push(new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 240, after: 120 }, children: [new TextRun({ text: "2. Rozkład godzin na działy", bold: true, size: 26, font: "Calibri", color: ACCENT })] }));

{
  const cols = [900, 6100, 2638];
  const rows = [new TableRow({ tableHeader: true, children: [hcell("Dział", cols[0]), hcell("Nazwa działu", cols[1]), hcell("Liczba godzin", cols[2])] })];
  dzialy.forEach((d, i) => {
    const fill = i % 2 ? GRAY : undefined;
    rows.push(new TableRow({ children: [
      cell([new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 }, children: [new TextRun({ text: d.nr, bold: true, size: 20, font: "Calibri" })] })], cols[0], { fill, valign: "center" }),
      cell([new Paragraph({ spacing: { after: 0 }, children: [new TextRun({ text: d.tytul, size: 20, font: "Calibri" })] })], cols[1], { fill, valign: "center" }),
      cell([new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 }, children: [new TextRun({ text: String(d.godziny), size: 20, font: "Calibri" })] })], cols[2], { fill, valign: "center" })
    ]}));
  });
  rows.push(new TableRow({ children: [
    cell([new Paragraph({ spacing: { after: 0 }, children: [] })], cols[0], { fill: HEAD }),
    cell([new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { after: 0 }, children: [new TextRun({ text: "Razem:", bold: true, size: 20, font: "Calibri" })] })], cols[1], { fill: HEAD }),
    cell([new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 }, children: [new TextRun({ text: String(RAZEM), bold: true, size: 20, font: "Calibri" })] })], cols[2], { fill: HEAD, valign: "center" })
  ]}));
  body.push(new Table({ columnWidths: cols, width: { size: W, type: WidthType.DXA }, rows }));
}

body.push(new Paragraph({ children: [new PageBreak()] }));
body.push(new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { after: 160 }, children: [new TextRun({ text: "3. Wymagania szczegółowe na poszczególne oceny", bold: true, size: 26, font: "Calibri", color: ACCENT })] }));

dzialy.forEach((d, idx) => {
  if (idx > 0) body.push(new Paragraph({ children: [new PageBreak()] }));
  body.push(new Paragraph({
    heading: HeadingLevel.HEADING_2, spacing: { before: 120, after: 100 },
    children: [new TextRun({ text: `Dział ${d.nr}. ${d.tytul}`, bold: true, size: 24, font: "Calibri", color: ACCENT })]
  }));
  body.push(P(`Liczba godzin: ${d.godziny}`, { italics: true, size: 19, color: "595959", after: 100 }));
  body.push(tabelaTematow(d));
  body.push(P("", { after: 140 }));
  body.push(tabelaWymagan(d));
});

const doc = new Document({
  creator: "PCEiKZ Szczucin",
  title: "Wymagania edukacyjne z informatyki – klasa 1W, branżowa szkoła I stopnia",
  description: "Wymagania edukacyjne opracowane na podstawie rozkładu materiału 1W i planu wynikowego dla branżowej szkoły I stopnia",
  numbering: {
    config: [{
      reference: "punkty",
      levels: [{
        level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 260, hanging: 180 } } }
      }]
    }]
  },
  styles: {
    default: { document: { run: { font: "Calibri", size: 21 } } }
  },
  sections: [{
    properties: { page: { margin: { top: 1134, right: 1134, bottom: 1134, left: 1134 } } },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [new TextRun({ children: ["Wymagania edukacyjne – informatyka, klasa 1W   |   s. ", PageNumber.CURRENT], size: 17, color: "808080", font: "Calibri" })]
        })]
      })
    },
    children: body
  }]
});

Packer.toBuffer(doc).then(b => {
  // Zapis prosto tam, skąd bierze go strona — żeby plik do pobrania nigdy
// nie rozjechał się z wymaganiami wypisanymi na stronie wymagań.
  const cel = require("path").join(__dirname, "..", "docs", "pliki",
                                   "wymagania-edukacyjne-informatyka-1w.docx");
  fs.writeFileSync(cel, b);
  console.log("OK", b.length, "bajtów →", cel);
});
