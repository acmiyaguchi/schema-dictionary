<script>
  import throttle from "just-throttle";

  import SchemaNode from "./SchemaNode.svelte";
  export let nodes = [];
  let filterText = "";
  let nodesWithVisibility;

  const filterTextChanged = () => {
    const filterTerms = filterText
      .trim()
      .split(" ")
      .filter(t => t.length > 0);

    const addVisibility = node => {
      node.fields && node.fields.forEach(addVisibility);
      node.visible =
        filterTerms.length === 0 ||
        filterTerms.every(term => node.name.includes(term));
      node.childrenVisible =
        node.fields &&
        node.fields.some(child => child.visible || child.childrenVisible);
      return node;
    };

    nodesWithVisibility = nodes.map(addVisibility, filterTerms);
  };

  filterTextChanged();
</script>

<style>
  .schema-browser {
    @apply p-2;
    @apply border-4;
    @apply border-gray-400;
    max-height: 400px;
    overflow: scroll;
  }
</style>

<h2>Schema</h2>
<div class="container py-4 mx-auto">
  <input
    class="shadow appearance-none border rounded w-full p-2 text-gray-700
    leading-tight focus:outline-none focus:shadow-outline"
    type="text"
    bind:value={filterText}
    on:input={throttle(filterTextChanged, 200)}
    placeholder="filter terms" />
</div>
<div class="container schema-browser mx-auto">
  <p>
    {#each nodesWithVisibility as node}
      <SchemaNode {node} />
    {/each}
  </p>
</div>
