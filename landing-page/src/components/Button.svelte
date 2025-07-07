<script lang="js">
  import { clsx } from 'clsx';
  let { class: className, children, variant = 'accent', ...restProps } = $props();
  const baseClasses = 'inline-flex rounded-full px-5 py-3 font-medium text-sm';
  const variantClasses = {
    accent: 'bg-indigo-500 text-white hover:bg-indigo-600',
    outline: 'border-2 border-indigo-500 text-indigo-500 hover:bg-indigo-500 hover:text-white'
  };
</script>

<button class={clsx(baseClasses, variantClasses[variant], className)} {...restProps}
  >{@render children()}</button
>
