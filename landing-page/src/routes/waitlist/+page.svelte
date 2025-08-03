<script lang="js">
  import { CaretLineRight } from 'phosphor-svelte';

  let hasConsented = $state(false);
</script>

<div
  class="mt-24 box-border flex min-h-[80vh] flex-col items-center justify-center gap-14 p-6 py-[100px] lg:p-8 lg:py-[100px]"
>
  <div class="flex flex-col items-start justify-center gap-7 md:items-center">
    <div
      class="text-heading-40 md:text-heading-48 lg:text-heading-56 text-foreground-primary font-geist-sans text-start md:text-center"
    >
      Join the Waitlist for Early Access
    </div>
    <div
      class="text-subheading-20-medium md:text-subheading-24-medium lg:text-subheading-32-medium text-foreground-secondary font-geist-sans md:text-center"
    >
      Be the first to simplify heat pump design with speed and precision
    </div>
  </div>
  <form class="grid grid-cols-1 items-center space-y-5" action="https://submit-form.com/echo">
    <input
      type="text"
      name="name"
      placeholder="John Doe"
      class="bg-component-default/50 text-foreground-secondary rounded-md border-0 outline-none"
      required="required"
    />
    <input
      type="email"
      name="email"
      placeholder="john.doe@example.com"
      class="bg-component-default/50 text-foreground-secondary rounded-md border-0 outline-none"
      required="required"
    />
    <label for="consent" class="inline-flex items-center gap-2">
      <input
        type="checkbox"
        bind:checked={hasConsented}
        id="consent"
        required="required"
        class="border-border-default bg-component-default checked:bg-foreground-secondary focus:ring-foreground-secondary focus:ring-offset-component-default h-5 w-5 appearance-none rounded border-2 checked:border-transparent focus:ring-1 focus:ring-offset-2"
        name="consent"
      />
      <div class="text-copy-16-light font-geist-sans text-foreground-secondary">
        I agree to receive ThermaSim updates and consent to the <a
          href="/privacy"
          class="underline underline-offset-6">privacy policy</a
        >.
      </div>
    </label>
    <div class="inline-flex items-center gap-2">
      <CaretLineRight class="text-foreground-secondary text-[14px] lg:text-[16px]" weight="bold" />
      <div class="text-copy-16-light text-foreground-secondary font-geist-sans">
        Your email is safe—only used for ThermaSim updates.
      </div>
    </div>
    <button
      type="submit"
      class="bg-component-default hover:bg-component-hover active:bg-component-active text-foreground-primary text-button-14-medium lg:text-button-16-medium font-geist-sans rounded-full p-3"
      >Sign Up
    </button>
  </form>
</div>
