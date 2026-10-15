/**
 * Original illustrative example, not sourced from the book.
 * Refactor a pricing rule into a pure, testable calculation.
 */

type LineItem = Readonly<{ unitPriceCents: number; quantity: number }>;

export function calculateSubtotalCents(items: readonly LineItem[]): number {
  return items.reduce((total, item) => {
    if (!Number.isSafeInteger(item.unitPriceCents) || item.unitPriceCents < 0) {
      throw new RangeError("unitPriceCents must be a non-negative safe integer");
    }
    if (!Number.isSafeInteger(item.quantity) || item.quantity < 0) {
      throw new RangeError("quantity must be a non-negative safe integer");
    }
    const lineTotal = item.unitPriceCents * item.quantity;
    if (!Number.isSafeInteger(lineTotal) || !Number.isSafeInteger(total + lineTotal)) {
      throw new RangeError("subtotal exceeds safe integer range");
    }
    return total + lineTotal;
  }, 0);
}

// Test ideas:
// - empty array -> 0
// - one or multiple items -> expected exact cents
// - zero quantity -> 0
// - invalid/negative/fractional input -> RangeError
// - unsafe multiplication or total overflow -> RangeError
