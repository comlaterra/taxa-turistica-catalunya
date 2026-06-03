// OCR d'un PDF amb el motor natiu de macOS (Vision + PDFKit). Sense dependències externes.
// Ús:  swift ocr_pdf.swift <fitxer.pdf>
// Surt: per cada fragment reconegut, una línia "PAGE\tx\ty\ttext" (coordenades normalitzades,
//        origen a baix-esquerra) per poder reconstruir files i columnes de taula.
import Foundation
import PDFKit
import Vision
import CoreGraphics

let args = CommandLine.arguments
guard args.count >= 2, let doc = PDFDocument(url: URL(fileURLWithPath: args[1])) else {
    FileHandle.standardError.write("No s'ha pogut obrir el PDF\n".data(using: .utf8)!)
    exit(1)
}

// Args opcionals: [2]=escala (per defecte 3.0), [3]="nocorrect" per desactivar la correcció
// lingüística (millor per a xifres).
let scale: CGFloat = args.count >= 3 ? (CGFloat(Double(args[2]) ?? 3.0)) : 3.0
let noCorrect = args.count >= 4 && args[3] == "nocorrect"
for i in 0..<doc.pageCount {
    guard let page = doc.page(at: i) else { continue }
    let rect = page.bounds(for: .mediaBox)
    let w = Int(rect.width * scale), h = Int(rect.height * scale)
    guard w > 0, h > 0,
          let ctx = CGContext(data: nil, width: w, height: h, bitsPerComponent: 8, bytesPerRow: 0,
                              space: CGColorSpaceCreateDeviceRGB(),
                              bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue) else { continue }
    ctx.setFillColor(CGColor(red: 1, green: 1, blue: 1, alpha: 1))
    ctx.fill(CGRect(x: 0, y: 0, width: w, height: h))
    ctx.saveGState()
    ctx.scaleBy(x: scale, y: scale)
    ctx.translateBy(x: -rect.minX, y: -rect.minY)
    page.draw(with: .mediaBox, to: ctx)
    ctx.restoreGState()
    guard let cg = ctx.makeImage() else { continue }

    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.usesLanguageCorrection = !noCorrect
    req.recognitionLanguages = ["ca-ES", "es-ES"]
    let handler = VNImageRequestHandler(cgImage: cg, options: [:])
    try? handler.perform([req])
    for obs in (req.results ?? []) {
        guard let top = obs.topCandidates(1).first else { continue }
        let bb = obs.boundingBox // normalitzat, origen baix-esquerra
        let line = "\(i+1)\t\(String(format: "%.4f", bb.minX))\t\(String(format: "%.4f", bb.midY))\t\(top.string)"
        print(line)
    }
}
